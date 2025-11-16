import moderngl_window as mglw
from moderngl_window import geometry
from pyrr import Matrix44

class App(mglw.WindowConfig):
    title = "Eclipse – test kuli"
    window_size = (1280, 720)
    resource_dir = '.'  # żeby widział folder shaders/

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # program (shadery)
        self.prog = self.load_program(
            vertex_shader='shaders/sphere.vert',
            fragment_shader='shaders/sphere.frag'
        )

        # jedna kula (na razie Ziemia)
        self.sphere = geometry.sphere(radius=1.0, sectors=64, rings=32)

        # macierze
        self.proj = Matrix44.perspective_projection(60.0, self.wnd.aspect_ratio, 0.1, 100.0)
        self.view = Matrix44.look_at(
            eye=(0.0, 0.0, 5.0),
            target=(0.0, 0.0, 0.0),
            up=(0.0, 1.0, 0.0)
        )

    def on_render(self, time: float, frametime: float):
        self.ctx.enable_only(self.ctx.DEPTH_TEST)
        self.ctx.clear(0.05, 0.05, 0.1)

        model = Matrix44.from_y_rotation(time * 0.3)  # kula się obraca

        self.prog['m_proj'].write(self.proj.astype('f4').tobytes())
        self.prog['m_view'].write(self.view.astype('f4').tobytes())
        self.prog['m_model'].write(model.astype('f4').tobytes())

        self.sphere.render(self.prog)

if __name__ == '__main__':
    mglw.run_window_config(App)
