from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy3 import Mesh, Material
from kivy3 import PerspectiveCamera
from kivy3 import Renderer, Scene
from kivy3.extras.geometries import BoxGeometry
from kivymd.uix.snackbar import MDSnackbar


class TD(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # create renderer
        self.renderer = Renderer()
        # create screen
        scene = Scene()
        # create default cube for scene
        cube_geo = BoxGeometry(1, 1, 1)
        cube_mat = Material()
        self.cube = Mesh(
            geometry=cube_geo,
            material=cube_mat
        )
        # default pos == (0, 0, 0)
        self.cube.pos.z = -5
        # create camera for scene
        self.camera = PerspectiveCamera(
            fov=75,  # distance from the scene
            aspect=0,  # 'screen' ratio
            near=1,  # nearest rendered point
            far=10  # farthest rendered point
        )
        # start rendering the scene and camera
        scene.add(self.cube)
        self.renderer.render(scene, self.camera)
        # set renderer ratio is its size changes ; Ex. when added to parent
        self.renderer.bind(size=self._adjust_aspect)

        self.add_widget(self.renderer)
        Clock.schedule_interval(self.rotate_cube, 1 / 60)  # FPS = 60
        Clock.max_iteration = 60

    def _adjust_aspect(self, *args):
        rsize = self.renderer.size
        aspect = rsize[0] / float(rsize[1])
        self.renderer.camera.aspect = aspect

    def rotate_cube(self, *dt):
        self.cube.rotation.y += 1
        # self.cube.rotation.z += 1
        # self.cube.rotation.x += 1


class RegularHexagonScreenView(Screen):

    def queans(self):
        side = self.ids.side_value.text
        if side != '':
            self.ids.area_value.text = str("{:.3f}".format(((3 * (3 ** (1 / 2))) / 2) * (float(side) ** 2)))
            self.ids.perimeter_value.text = str("{:.3f}".format(6 * float(side)))
        else:
            self.ids.area_value.text = ''
            self.ids.perimeter_value.text = ''
            MDSnackbar(text="[color=#ff6961]Please fill all the required blanks[/color]", ).open()
