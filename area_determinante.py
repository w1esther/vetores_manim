import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import TextBox

class LaboratorioAreaFixa:
    def __init__(self):
        # Matriz inicial M
        self.M = np.array([[2.0, 1.0], [4.0, 3.0]])
        self.pontos_originais = []
        
        self.fig = plt.figure(figsize=(16, 8))
        self.ax_esq = self.fig.add_subplot(131)
        self.ax_mid = self.fig.add_subplot(132)
        self.ax_ctrl = self.fig.add_subplot(133)
        
        self.fig.subplots_adjust(bottom=0.2, right=0.95, wspace=0.3)
        self.fig.canvas.manager.set_window_title('Cálculo de Área e Transformação')

        # --- CONFIGURAÇÃO DE ZOOM FIXO ---
        # Definimos limites estáticos para que a escala não mude
        self.limite_esq = 6
        self.limite_mid = 25
        
        self._configurar_eixo(self.ax_esq, "Original", self.limite_esq)
        self._configurar_eixo(self.ax_mid, "Transformado", self.limite_mid)
        self.ax_ctrl.axis('off')

        # Elementos Visuais
        self.line_orig, = self.ax_esq.plot([], [], 'b-o', markersize=4)
        self.poly_orig = self.ax_esq.fill([], [], 'b', alpha=0.2)[0]
        self.line_trans, = self.ax_mid.plot([], [], 'r-s', markersize=4)
        self.poly_trans = self.ax_mid.fill([], [], 'r', alpha=0.2)[0]

        # Textos de Informação
        self.txt_info = self.ax_ctrl.text(0.05, 0.5, '', fontsize=12, family='monospace')

        # Widgets da Matriz
        self.inputs = []
        labels = ['a', 'b', 'c', 'd']
        for i in range(4):
            ax_box = self.fig.add_axes([0.78 + (i%2)*0.08, 0.8 - (i//2)*0.1, 0.05, 0.04])
            text_box = TextBox(ax_box, f"{labels[i]}: ", initial=str(self.M.flatten()[i]))
            text_box.on_submit(self._atualizar_matriz)
            self.inputs.append(text_box)

        self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.atualizar_visualizacao()

    def _configurar_eixo(self, ax, titulo, limite):
        ax.set_title(titulo)
        ax.set_xlim(-limite, limite)
        ax.set_ylim(-limite, limite)
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
        ax.set_aspect('equal') # Mantém a proporção geométrica correta

    def calcular_area(self, pts):
        """Implementa a Shoelace Formula: 0.5 * |sum(xi*yi+1 - xi+1*yi)|"""
        if len(pts) < 3: return 0.0
        x = pts[:, 0]
        y = pts[:, 1]
        return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

    def _atualizar_matriz(self, event):
        try:
            vals = [float(txt.text) for txt in self.inputs]
            self.M = np.array(vals).reshape(2, 2)
            self.atualizar_visualizacao()
        except ValueError: pass

    def onclick(self, event):
        if event.inaxes != self.ax_esq: return
        if event.button == 3: self.pontos_originais = []
        else: self.pontos_originais.append([event.xdata, event.ydata])
        self.atualizar_visualizacao()

    def atualizar_visualizacao(self):
        det = np.linalg.det(self.M)
        area_orig = 0.0
        area_trans = 0.0

        if self.pontos_originais:
            pts = np.array(self.pontos_originais)
            area_orig = self.calcular_area(pts)
            
            # Update Original
            pts_plot = np.vstack([pts, pts[0]])
            self.line_orig.set_data(pts_plot[:, 0], pts_plot[:, 1])
            self.poly_orig.set_xy(pts)

            # Update Transformado
            pts_trans = pts @ self.M.T
            area_trans = self.calcular_area(pts_trans)
            pts_trans_plot = np.vstack([pts_trans, pts_trans[0]])
            self.line_trans.set_data(pts_trans_plot[:, 0], pts_trans_plot[:, 1])
            self.poly_trans.set_xy(pts_trans)

        # Atualiza Painel de Texto
        self.txt_info.set_text(
            f"MATRIZ M:\n{self.M}\n\n"
            f"DET(M): {det:.4f}\n\n"
            f"ÁREA ORIG:  {area_orig:.4f}\n"
            f"ÁREA TRANS: {area_trans:.4f}\n\n"
            f"RAZÃO ÁREAS: { (area_trans/area_orig) if area_orig != 0 else 0:.4f}"
        )
        self.fig.canvas.draw_idle()

if __name__ == "__main__":
    lab = LaboratorioAreaFixa()
    plt.show()