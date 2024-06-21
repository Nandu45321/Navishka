from View.MainScreen.main_screen import MainScreenView
from View.Shapes.ThreeD.CubeScreen.cube_screen import CubeScreenView
from View.Shapes.ThreeD.CuboidScreen.cuboid_screen import CuboidScreenView
from View.Shapes.ThreeD.SphereScreen.sphere_screen import SphereScreenView
from View.Shapes.TwoD.CircleScreen.circle_screen import CircleScreenView
from View.Shapes.TwoD.EllipseScreen.ellipse_screen import EllipseScreenView
from View.Shapes.TwoD.EquilateralTriangleScreen.equilateral_triangle_screen import EquilateralTriangleScreenView
from View.Shapes.TwoD.KiteScreen.kite_screen import KiteScreenView
from View.Shapes.TwoD.ParallelogramScreen.parallelogram_screen import ParallelogramScreenView
from View.Shapes.TwoD.QuadrilateralScreen.quadrilateral_screen import QuadrilateralScreenView
from View.Shapes.TwoD.RectangleScreen.rectangle_screen import RectangleScreenView
from View.Shapes.TwoD.RegularDecagonScreen.regular_decagon_screen import RegularDecagonScreenView
from View.Shapes.TwoD.RegularHeptagonScreen.regular_heptagon_screen import RegularHeptagonScreenView
from View.Shapes.TwoD.RegularHexagonScreen.regular_hexagon_screen import RegularHexagonScreenView
from View.Shapes.TwoD.RegularNonagonScreen.regular_nonagon_screen import RegularNonagonScreenView
from View.Shapes.TwoD.RegularOctagonScreen.regular_octagon_screen import RegularOctagonScreenView
from View.Shapes.TwoD.RegularPentagonScreen.regular_pentagon_screen import RegularPentagonScreenView
from View.Shapes.TwoD.RhombusScreen.rhombus_screen import RhombusScreenView
from View.Shapes.TwoD.RightTriangleScreen.right_triangle_screen import RightTriangleScreenView
from View.Shapes.TwoD.ScaleneTriangleScreen.scalene_triangle_screen import ScaleneTriangleScreenView
from View.Shapes.TwoD.SemiCircleScreen.semi_circle_screen import SemiCircleScreenView
from View.Shapes.TwoD.SquareScreen.square_screen import SquareScreenView
from View.Shapes.TwoD.TrapeziumScreen.trapezium_screen import TrapeziumScreenView
from View.Shapes.TwoD.TriangleScreen.triangle_screen import TriangleScreenView
from View.Shapes.ThreeD.TriangularPrismScreen.triangular_prism_screen import TriangularPrismScreenView
from View.Shapes.ThreeD.TriangularPyramidScreen.triangular_pyramid_screen import TriangularPyramidScreenView
from View.Shapes.ThreeD.SquarePyramidScreen.square_pyramid_screen import SquarePyramidScreenView

screens = {
    "main screen": {"view": MainScreenView, "kv": "View/MainScreen/main_screen.kv"},
    "triangle screen": {"view": TriangleScreenView, "kv": "View/Shapes/TwoD/TriangleScreen/triangle_screen.kv"},
    "equilateral triangle screen": {"view": EquilateralTriangleScreenView,
                                    "kv": "View/Shapes/TwoD/EquilateralTriangleScreen/equilateral_triangle_screen.kv"},
    "right triangle screen": {"view": RightTriangleScreenView,
                              "kv": "View/Shapes/TwoD/RightTriangleScreen/right_triangle_screen.kv"},
    "scalene triangle screen": {"view": ScaleneTriangleScreenView,
                                "kv": "View/Shapes/TwoD/ScaleneTriangleScreen/scalene_triangle_screen.kv"},
    "quadrilateral screen": {"view": QuadrilateralScreenView,
                             "kv": "View/Shapes/TwoD/QuadrilateralScreen/quadrilateral_screen.kv"},
    "trapezium screen": {"view": TrapeziumScreenView, "kv": "View/Shapes/TwoD/TrapeziumScreen/trapezium_screen.kv"},
    "parallelogram screen": {"view": ParallelogramScreenView,
                             "kv": "View/Shapes/TwoD/ParallelogramScreen/parallelogram_screen.kv"},
    "rectangle screen": {"view": RectangleScreenView, "kv": "View/Shapes/TwoD/RectangleScreen/rectangle_screen.kv"},
    "square screen": {"view": SquareScreenView, "kv": "View/Shapes/TwoD/SquareScreen/square_screen.kv"},
    "rhombus screen": {"view": RhombusScreenView, "kv": "View/Shapes/TwoD/RhombusScreen/rhombus_screen.kv"},
    "kite screen": {"view": KiteScreenView, "kv": "View/Shapes/TwoD/KiteScreen/kite_screen.kv"},
    "regular pentagon screen": {"view": RegularPentagonScreenView,
                                "kv": "View/Shapes/TwoD/RegularPentagonScreen/regular_pentagon_screen.kv"},
    "regular hexagon screen": {"view": RegularHexagonScreenView,
                               "kv": "View/Shapes/TwoD/RegularHexagonScreen/regular_hexagon_screen.kv"},
    "regular heptagon screen": {"view": RegularHeptagonScreenView,
                                "kv": "View/Shapes/TwoD/RegularHeptagonScreen/regular_heptagon_screen.kv"},
    "regular octagon screen": {"view": RegularOctagonScreenView,
                               "kv": "View/Shapes/TwoD/RegularOctagonScreen/regular_octagon_screen.kv"},
    "regular nonagon screen": {"view": RegularNonagonScreenView,
                               "kv": "View/Shapes/TwoD/RegularNonagonScreen/regular_nonagon_screen.kv"},
    "regular decagon screen": {"view": RegularDecagonScreenView,
                               "kv": "View/Shapes/TwoD/RegularDecagonScreen/regular_decagon_screen.kv"},
    "circle screen": {"view": CircleScreenView, "kv": "View/Shapes/TwoD/CircleScreen/circle_screen.kv"},
    "semi circle screen": {"view": SemiCircleScreenView,
                           "kv": "View/Shapes/TwoD/SemiCircleScreen/semi_circle_screen.kv"},
    "ellipse screen": {"view": EllipseScreenView, "kv": "View/Shapes/TwoD/EllipseScreen/ellipse_screen.kv"},
    "sphere screen": {"view": SphereScreenView, "kv": "View/Shapes/ThreeD/SphereScreen/sphere_screen.kv"},
    "cube screen": {"view": CubeScreenView, "kv": "View/Shapes/ThreeD/CubeScreen/cube_screen.kv"},
    "cuboid screen": {"view": CuboidScreenView, "kv": "View/Shapes/ThreeD/CuboidScreen/cuboid_screen.kv"},
    "triangular prism screen": {"view": TriangularPrismScreenView,
                                "kv": "View/Shapes/ThreeD/TriangularPrismScreen/triangular_prism_screen.kv"},
    "triangular pyramid screen": {"view": TriangularPyramidScreenView,
                                  "kv": "View/Shapes/ThreeD/TriangularPyramidScreen/triangular_pyramid_screen.kv"},
    "square pyramid screen": {"view": SquarePyramidScreenView,
                              "kv": "View/Shapes/ThreeD/SquarePyramidScreen/square_pyramid_screen.kv"}
}
