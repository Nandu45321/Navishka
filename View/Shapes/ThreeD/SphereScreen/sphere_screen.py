from random import random

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy3 import Mesh, Material
from kivy3 import PerspectiveCamera
from kivy3 import Renderer, Scene
from kivy3.extras.geometries import BoxGeometry
from kivymd.uix.snackbar import MDSnackbar


class ThreeD(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        # create renderer
        self.renderer = Renderer(size_hint=(5, 5))
        self.renderer.set_clear_color(
            (0.1, 0.1, 0.1, 1)  # rgba
        )
        # create screen
        scene = Scene()
        self.cubes = []
        # create cubes for scene
        #
        # CUBES
        # default pure green cube                                            # 1
        cube_geo = BoxGeometry(1, 1, 1)
        cube_mat = Material(
            color=(0, 0.5, 0)  # base color
        )
        self.cubes.append(Mesh(
            geometry=cube_geo,
            material=cube_mat
        ))
        # default pos == (0, 0, 0)
        self.cubes[0].pos.z = -5
        self.cubes[0].pos.x = 1
        self.cubes[0].pos.y = 0.8
        self.cubes[0].rotation.x = 45

        # black cube, red shadow, half-tranparent                             # 2
        cube_geo = BoxGeometry(1, 1, 1)
        cube_mat = Material(
            transparency=0.5,
            color=(0, 0, 0),  # base color
            diffuse=(10, 5, 4),  # color of shadows
            specular=(1, 0, 0)  # mirror-like reflections
        )
        self.cubes.append(Mesh(
            geometry=cube_geo,
            material=cube_mat
        ))
        # default pos == (0, 0, 0)
        self.cubes[1].pos.z = -5
        self.cubes[1].pos.x = -1
        self.cubes[1].pos.y = 0.8
        self.cubes[1].rotation.y = 45

        # default pure green cube, with red reflections                        # 3
        cube_geo = BoxGeometry(1, 1, 1)
        cube_mat = Material(
            transparency=1,
            color=(0, 0.5, 0),  # base color
            diffuse=(0, 0, 0),  # color of shadows
            specular=(10, 0, 0)  # mirror-like reflections
        )
        self.cubes.append(Mesh(
            geometry=cube_geo,
            material=cube_mat
        ))
        # default pos == (0, 0, 0)
        self.cubes[2].pos.z = -5
        self.cubes[2].pos.x = 1
        self.cubes[2].pos.y = -0.8
        self.cubes[2].rotation.z = 45

        # black cube, with red reflections, half-transparent                    # 4
        cube_geo = BoxGeometry(1, 1, 1)
        cube_mat = Material(
            transparency=0.5,
            color=(0, 0, 0),  # base color
            specular=(10, 0, 0)  # mirror-like reflections
        )
        self.cubes.append(Mesh(
            geometry=cube_geo,
            material=cube_mat
        ))
        # default pos == (0, 0, 0)
        self.cubes[3].pos.z = -5
        self.cubes[3].pos.x = -1
        self.cubes[3].pos.y = -0.8
        self.cubes[3].rotation.x = 45

        #
        # create camera for scene
        self.camera = PerspectiveCamera(
            fov=75,  # distance from the scene
            aspect=0,  # 'screen' ratio
            near=1,  # nearest rendered point
            far=10  # farthest rendered point
        )
        # start rendering the scene and camera
        for cube in self.cubes:
            scene.add(cube)

        self.renderer.render(scene, self.camera)
        # set renderer ratio is its size changes ; Ex. when added to parent
        self.renderer.bind(size=self._adjust_aspect)

        for _ in range(4):
            self.add_widget(Label())
        self.add_widget(self.renderer)

        for t in ['+n\nY\n\n-', '-     X     +']:
            self.add_widget(Label(text=t))
            self.add_widget(Label())

        Clock.schedule_interval(self.rotate_cube, 1 / 60)  # FPS = 60
        Clock.schedule_interval(self.scale_cube, 1 / 4)
        Clock.max_iteration = 60

    def _adjust_aspect(self, *args):
        rsize = self.renderer.size
        aspect = rsize[0] / float(rsize[1])
        self.renderer.camera.aspect = aspect

    def rotate_cube(self, *dt):
        for cube in self.cubes:
            cube.rotation.y += 1
            cube.rotation.z += 1
        # self.cube.rotation.x += 1

    def scale_cube(self, *dt):
        for cube in self.cubes:
            factor = random()
            # cube.scale.x = factor
            # cube.scale.y = factor
            # cube.scale.z = factor
            anim = Animation(x=factor)
            anim &= Animation(y=factor)
            anim &= Animation(z=factor)
            anim.start(cube.scale)


class SphereScreenView(Screen):

    def queans(self):
        radius_input = self.ids.radius_value.text
        if radius_input != '':
            self.ids.volume_value.hint_text = str(round((4 / 3) * 3.141592653589793238 * (float(radius_input) ** 3), 4))
            self.ids.tsa_value.hint_text = str(round(4 * 3.141592653589793238 * (float(radius_input) ** 2), 4))
        else:
            self.ids.volume_value.hint_text = ''
            self.ids.tsa_value.hint_text = ''
            MDSnackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()
