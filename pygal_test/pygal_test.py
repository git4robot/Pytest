'''A test for pygal.'''
from pygal import *
from webbrowser import open_new
from os import mkdir, getcwd
from math import cos

firefox1 = [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1]
firefox2 = [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450]
chrome1 = [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3]
chrome2 = [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607]
ie1 = [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1]
ie2 = [43, 41, 59, 79, 144, 136, 34, 102]
opera = [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669]
others = [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5]

def test1():
    line_chart = Line()
    line_chart.title = 'Browser Usage Evolution'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', firefox1)
    line_chart.add('Chrome', chrome1)
    line_chart.add('IE', ie1)
    line_chart.add('Others', others)
    line_chart.range = [0, 90]
    path = f'{getcwd()}\\data\\test1-1.svg'
    line_chart.render_to_file(path)
    open_new(path)

    line_chart = HorizontalLine()
    line_chart.title = 'Browser Usage Evolution'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', firefox1)
    line_chart.add('Chrome', chrome1)
    line_chart.add('IE', ie1)
    line_chart.add('Others', others)
    line_chart.range = [0, 90]
    path = f'{getcwd()}\\data\\test1-2.svg'
    line_chart.render_to_file(path)
    open_new(path)

    line_chart = StackedLine(fill = True)
    line_chart.title = 'Browser Usage Evolution'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', firefox1)
    line_chart.add('Chrome', chrome1)
    line_chart.add('IE', ie1)
    line_chart.add('Others', others)
    path = f'{getcwd()}\\data\\test1-3.svg'
    line_chart.render_to_file(path)
    open_new(path)

def test2():
    line_chart = Bar()
    line_chart.title = 'Browser Usage Evolution'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', firefox1)
    line_chart.add('Chrome', chrome1)
    line_chart.add('IE', ie1)
    line_chart.add('Others', others)
    path = f'{getcwd()}\\data\\test2-1.svg'
    line_chart.render_to_file(path)
    open_new(path)

    line_chart = StackedBar()
    line_chart.title = 'Browser Usage Evolution'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', firefox1)
    line_chart.add('Chrome', chrome1)
    line_chart.add('IE', ie1)
    line_chart.add('Others', others)
    path = f'{getcwd()}\\data\\test2-2.svg'
    line_chart.render_to_file(path)
    open_new(path)

    line_chart = HorizontalBar()
    line_chart.title = 'Browser Usage Evolution'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', firefox1)
    line_chart.add('Chrome', chrome1)
    line_chart.add('IE', ie1)
    line_chart.add('Others', others)
    path = f'{getcwd()}\\data\\test2-3.svg'
    line_chart.render_to_file(path)
    open_new(path)

def test3():
    xy_chart = XY()
    xy_chart.title = 'XY Cosinus'
    xy_chart.add('X = cos(y)', [(cos(x / 10.), x / 10.) for x in range(-50, 50, 5)])
    xy_chart.add('Y = cos(x)', [(x / 10., cos(x / 10.)) for x in range(-50, 50, 5)])
    xy_chart.add('X = 1',  [(1, -5), (1, 5)])
    xy_chart.add('X = -1', [(-1, -5), (-1, 5)])
    xy_chart.add('Y = 1',  [(-5, 1), (5, 1)])
    xy_chart.add('Y = -1', [(-5, -1), (5, -1)])
    path = f'{getcwd()}\\data\\test3-1.svg'
    xy_chart.render_to_file(path)
    open_new(path)

    xy_chart = XY(stroke = False)
    xy_chart.title = 'Correlation'
    xy_chart.add('A', [(0, 0), (.1, .2), (.3, .1), (.5, 1), (.8, .6), (1, 1.08), (1.3, 1.1), (2, 3.23), (2.43, 2)])
    xy_chart.add('B', [(.1, .15), (.12, .23), (.4, .3), (.6, .4), (.21, .21), (.5, .3), (.6, .8), (.7, .8)])
    xy_chart.add('C', [(.05, .01), (.13, .02), (1.5, 1.7), (1.52, 1.6), (1.8, 1.63), (1.5, 1.82), (1.7, 1.23), (2.1, 2.23), (2.3, 1.98)])
    path = f'{getcwd()}\\data\\test3-2.svg'
    xy_chart.render_to_file(path)
    open_new(path)

def test4():
    pie_chart = Pie()
    pie_chart.title = 'Browser Usage in Feb. 2012'
    pie_chart.add('IE', 19.5)
    pie_chart.add('Firefox', 36.6)
    pie_chart.add('Chrome', 36.3)
    pie_chart.add('Safari', 4.5)
    pie_chart.add('Opera', 2.3)
    path = f'{getcwd()}\\data\\test4-1.svg'
    pie_chart.render_to_file(path)
    open_new(path)

    pie_chart = Pie()
    pie_chart.title = 'Browser Usage by Version in Feb. 2012'
    pie_chart.add('IE', [5.7, 10.2, 2.6, 1])
    pie_chart.add('Firefox', [.6, 16.8, 7.4, 2.2, 1.2, 1, 1, 1.1, 4.3, 1])
    pie_chart.add('Chrome', [.3, .9, 17.1, 15.3, .6, .5, 1.6])
    pie_chart.add('Safari', [4.4, .1])
    pie_chart.add('Opera', [.1, 1.6, .1, .5])
    path = f'{getcwd()}\\data\\test4-2.svg'
    pie_chart.render_to_file(path)
    open_new(path)

    pie_chart = Pie(inner_radius = .4)
    pie_chart.title = 'Browser Usage by Version in Feb. 2012'
    pie_chart.add('IE', 19.5)
    pie_chart.add('Firefox', 36.6)
    pie_chart.add('Chrome', 36.3)
    pie_chart.add('Safari', 4.5)
    pie_chart.add('Opera', 2.3)
    path = f'{getcwd()}\\data\\test4-3.svg'
    pie_chart.render_to_file(path)
    open_new(path)

    pie_chart = Pie(half_pie = True)
    pie_chart.title = 'Browser Usage by Version in Feb. 2012'
    pie_chart.add('IE', 19.5)
    pie_chart.add('Firefox', 36.6)
    pie_chart.add('Chrome', 36.3)
    pie_chart.add('Safari', 4.5)
    pie_chart.add('Opera', 2.3)
    path = f'{getcwd()}\\data\\test4-4.svg'
    pie_chart.render_to_file(path)
    open_new(path)

def test5():
    radar_chart = Radar()
    radar_chart.title = 'V8 Benchmark Results'
    radar_chart.x_labels = ['Richards', 'DeltaBlue', 'Crypto', 'RayTrace', 'EarleyBoyer', 'RegExp', 'Splay', 'NavierStokes']
    radar_chart.add('Chrome', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])
    radar_chart.add('Firefox', firefox2)
    radar_chart.add('Opera', opera)
    radar_chart.add('IE', ie2)
    path = f'{getcwd()}\\data\\test5.svg'
    radar_chart.render_to_file(path)
    open_new(path)

def test6():
    box_plot = Box()
    box_plot.title = 'V8 Benchmark Results'
    box_plot.add('Chrome', chrome2)
    box_plot.add('Firefox', firefox2)
    box_plot.add('Opera', opera)
    box_plot.add('IE', ie2)
    path = f'{getcwd()}\\data\\test6-1.svg'
    box_plot.render_to_file(path)
    open_new(path)

    box_plot = Box(box_mode = 'stdev')
    box_plot.title = 'V8 Benchmark Results'
    box_plot.add('Chrome', chrome2)
    box_plot.add('Firefox', firefox2)
    box_plot.add('Opera', opera)
    box_plot.add('IE', ie2)
    path = f'{getcwd()}\\data\\test6-2.svg'
    box_plot.render_to_file(path)
    open_new(path)

    box_plot = Box(box_mode = 'pstdev')
    box_plot.title = 'V8 Benchmark Results'
    box_plot.add('Chrome', chrome2)
    box_plot.add('Firefox', firefox2)
    box_plot.add('Opera', opera)
    box_plot.add('IE', ie2)
    path = f'{getcwd()}\\data\\test6-3.svg'
    box_plot.render_to_file(path)
    open_new(path)

def test7():
    dot_chart = Dot(x_label_rotation = 30)
    dot_chart.title = 'V8 Benchmark Results'
    dot_chart.x_labels = ['Richards', 'DeltaBlue', 'Crypto', 'RayTrace', 'EarleyBoyer', 'RegExp', 'Splay', 'NavierStokes']
    dot_chart.add('Chrome', chrome2)
    dot_chart.add('Firefox', firefox2)
    dot_chart.add('Opera', opera)
    dot_chart.add('IE', ie2)
    path = f'{getcwd()}\\data\\test7.svg'
    dot_chart.render_to_file(path)
    open_new(path)

def test8():
    funnel_chart = Funnel(x_label_rotation = 30)
    funnel_chart.title = 'V8 Benchmark Results'
    funnel_chart.x_labels = ['Richards', 'DeltaBlue', 'Crypto', 'RayTrace', 'EarleyBoyer', 'RegExp', 'Splay', 'NavierStokes']
    funnel_chart.add('Chrome', chrome2)
    funnel_chart.add('Firefox', firefox2)
    funnel_chart.add('Opera', opera)
    funnel_chart.add('IE', ie2)
    path = f'{getcwd()}\\data\\test8.svg'
    funnel_chart.render_to_file(path)
    open_new(path)

def test9():
    gauge = SolidGauge(inner_radius = .70)
    gauge.title = 'Solid Gauge and Formatter'
    percent_formatter = lambda x: f'{x:.10g}%'
    dollar_formatter = lambda x: f'{x:.10g}$'
    gauge.value_formatter = percent_formatter
    gauge.add('Series 1', [{'value': 225000, 'max_value': 1275000}], formatter = dollar_formatter)
    gauge.add('Series 2', [{'value': 110, 'max_value': 100}])
    gauge.add('Series 3', [{'value': 3}])
    gauge.add('Series 4', [{'value': 51, 'max_value': 100}, {'value': 12, 'max_value': 100}])
    gauge.add('Series 5', [{'value': 79, 'max_value': 100}])
    gauge.add('Series 6', 99)
    gauge.add('Series 7', [{'value': 100, 'max_value': 100}])
    path = f'{getcwd()}\\data\\test9-1.svg'
    gauge.render_to_file(path)
    open_new(path)

    gauge = SolidGauge(half_pie = True, inner_radius = .70, style = style.styles['default'](value_font_size = 10))
    gauge.title = 'Solid Gauge and Formatter'
    percent_formatter = lambda x: f'{x:.10g}%'
    dollar_formatter = lambda x: f'{x:.10g}$'
    gauge.value_formatter = percent_formatter
    gauge.add('Series 1', [{'value': 225000, 'max_value': 1275000}], formatter = dollar_formatter)
    gauge.add('Series 2', [{'value': 110, 'max_value': 100}])
    gauge.add('Series 3', [{'value': 3}])
    gauge.add('Series 4', [{'value': 51, 'max_value': 100}, {'value': 12, 'max_value': 100}])
    gauge.add('Series 5', [{'value': 79, 'max_value': 100}])
    gauge.add('Series 6', 99)
    gauge.add('Series 7', [{'value': 100, 'max_value': 100}])
    path = f'{getcwd()}\\data\\test9-2.svg'
    gauge.render_to_file(path)
    open_new(path)

def test10():
    gauge_chart = Gauge(human_readable = True)
    gauge_chart.title = 'DeltaBlue V8 Benchmark Results'
    gauge_chart.range = [0, 10000]
    gauge_chart.add('Chrome', 8212)
    gauge_chart.add('Firefox', 8099)
    gauge_chart.add('Opera', 2933)
    gauge_chart.add('IE', 41)
    path = f'{getcwd()}\\data\\test10.svg'
    gauge_chart.render_to_file(path)
    open_new(path)

def test11():
    ages = [(364381, 358443, 360172, 345848, 334895, 326914, 323053, 312576, 302015, 301277, 309874, 318295, 323396, 332736, 330759, 335267, 345096, 352685, 368067, 381521, 380145, 378724, 388045, 382303, 373469, 365184, 342869, 316928, 285137, 273553, 250861, 221358, 195884, 179321, 171010, 162594, 152221, 148843, 143013, 135887, 125824, 121493, 115913, 113738, 105612, 99596, 91609, 83917, 75688, 69538, 62999, 58864, 54593, 48818, 44739, 41096, 39169, 36321, 34284, 32330, 31437, 30661, 31332, 30334, 23600, 21999, 20187, 19075, 16574, 15091, 14977, 14171, 13687, 13155, 12558, 11600, 10827, 10436, 9851, 9794, 8787, 7993, 6901, 6422, 5506, 4839, 4144, 3433, 2936, 2615),
   (346205, 340570, 342668, 328475, 319010, 312898, 308153, 296752, 289639, 290466, 296190, 303871, 309886, 317436, 315487, 316696, 325772, 331694, 345815, 354696, 354899, 351727, 354579, 341702, 336421, 321116, 292261, 261874, 242407, 229488, 208939, 184147, 162662, 147361, 140424, 134336, 126929, 125404, 122764, 116004, 105590, 100813, 95021, 90950, 85036, 79391, 72952, 66022, 59326, 52716, 46582, 42772, 38509, 34048, 30887, 28053, 26152, 23931, 22039, 20677, 19869, 19026, 18757, 18308, 14458, 13685, 12942, 12323, 11033, 10183, 10628, 10803, 10655, 10482, 10202, 10166, 9939, 10138, 10007, 10174, 9997, 9465, 9028, 8806, 8450, 7941, 7253, 6698, 6267, 5773),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 91, 412, 1319, 2984, 5816, 10053, 16045, 24240, 35066, 47828, 62384, 78916, 97822, 112738, 124414, 130658, 140789, 153951, 168560, 179996, 194471, 212006, 225209, 228886, 239690, 245974, 253459, 255455, 260715, 259980, 256481, 252222, 249467, 240268, 238465, 238167, 231361, 223832, 220459, 222512, 220099, 219301, 221322, 229783, 239336, 258360, 271151, 218063, 213461, 207617, 196227, 174615, 160855, 165410, 163070, 157379, 149698, 140570, 131785, 119936, 113751, 106989, 99294, 89097, 78413, 68174, 60592, 52189, 43375, 35469, 29648, 24575, 20863),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 392, 1351, 3906, 7847, 12857, 19913, 29108, 42475, 58287, 74163, 90724, 108375, 125886, 141559, 148061, 152871, 159725, 171298, 183536, 196136, 210831, 228757, 238731, 239616, 250036, 251759, 259593, 261832, 264864, 264702, 264070, 258117, 253678, 245440, 241342, 239843, 232493, 226118, 221644, 223440, 219833, 219659, 221271, 227123, 232865, 250646, 261796, 210136, 201824, 193109, 181831, 159280, 145235, 145929, 140266, 133082, 124350, 114441, 104655, 93223, 85899, 78800, 72081, 62645, 53214, 44086, 38481, 32219, 26867, 21443, 16899, 13680, 11508),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 5, 17, 15, 31, 34, 38, 35, 45, 299, 295, 218, 247, 252, 254, 222, 307, 316, 385, 416, 463, 557, 670, 830, 889, 1025, 1149, 1356, 1488, 1835, 1929, 2130, 2362, 2494, 2884, 3160, 3487, 3916, 4196, 4619, 5032, 5709, 6347, 7288, 8139, 9344, 11002, 12809, 11504, 11918, 12927, 13642, 13298, 14015, 15751, 17445, 18591, 19682, 20969, 21629, 22549, 23619, 25288, 26293, 27038, 27039, 27070, 27750, 27244, 25905, 24357, 22561, 21794, 20595),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 8, 0, 8, 21, 34, 49, 84, 97, 368, 401, 414, 557, 654, 631, 689, 698, 858, 1031, 1120, 1263, 1614, 1882, 2137, 2516, 2923, 3132, 3741, 4259, 4930, 5320, 5948, 6548, 7463, 8309, 9142, 10321, 11167, 12062, 13317, 15238, 16706, 18236, 20336, 23407, 27024, 32502, 37334, 34454, 38080, 41811, 44490, 45247, 46830, 53616, 58798, 63224, 66841, 71086, 73654, 77334, 82062, 87314, 92207, 94603, 94113, 92753, 93174, 91812, 87757, 84255, 79723, 77536, 74173),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 0, 11, 35, 137, 331, 803, 1580, 2361, 3632, 4866, 6849, 8754, 10422, 12316, 14152, 16911, 19788, 22822, 27329, 31547, 35711, 38932, 42956, 46466, 49983, 52885, 55178, 56549, 57632, 57770, 57427, 56348, 55593, 55554, 53266, 51084, 49342, 48555, 47067, 45789, 44988, 44624, 44238, 46267, 46203, 36964, 33866, 31701, 28770, 25174, 22702, 21934, 20638, 19051, 17073, 15381, 13736, 11690, 10368, 9350, 8375, 7063, 6006, 5044, 4030, 3420, 2612, 2006, 1709, 1264, 1018),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 11, 20, 68, 179, 480, 1077, 2094, 3581, 5151, 7047, 9590, 12434, 15039, 17257, 19098, 21324, 24453, 27813, 32316, 37281, 43597, 49647, 53559, 58888, 62375, 67219, 70956, 73547, 74904, 75994, 76224, 74979, 72064, 70330, 68944, 66527, 63073, 60899, 60968, 58756, 57647, 56301, 57246, 57068, 59027, 59187, 47549, 44425, 40976, 38077, 32904, 29431, 29491, 28020, 26086, 24069, 21742, 19498, 17400, 15738, 14451, 13107, 11568, 10171, 8530, 7273, 6488, 5372, 4499, 3691, 3259, 2657)]
    types = ['Males single', 'Females single', 'Males married', 'Females married', 'Males widowed', 'Females widowed', 'Males divorced', 'Females divorced']
    pyramid_chart = Pyramid(human_readable = True, legend_at_bottom = True)
    pyramid_chart.title = 'England Population by Age in 2010'
    pyramid_chart.x_labels = map(lambda x: str(x) if not x % 5 else '', range(90))
    for type, age in zip(types, ages): pyramid_chart.add(type, age)
        
    path = f'{getcwd()}\\data\\test11.svg'
    pyramid_chart.render_to_file(path)
    open_new(path)

def test12():
    treemap = Treemap()
    treemap.title = 'Binary TreeMap'
    treemap.add('A', [2, 1, 12, 4, 2, 1, 1, 3, 12, 3, 4, None, 9])
    treemap.add('B', [4, 2, 5, 10, 3, 4, 2, 7, 4, -10, None, 8, 3, 1])
    treemap.add('C', [3, 8, 3, 3, 5, 3, 3, 5, 4, 12])
    treemap.add('D', [23, 18])
    treemap.add('E', [1, 2, 1, 2, 3, 3, 1, 2, 3, 4, 3, 1, 2, 1, 1, 1, 1, 1])
    treemap.add('F', [31])
    treemap.add('G', [5, 9.3, 8.1, 12, 4, 3, 2])
    treemap.add('H', [12, 3, 3])
    path = f'{getcwd()}\\data\\test12.svg'
    treemap.render_to_file(path)
    open_new(path)

def test13():
    worldmap_chart = maps.world.World()
    worldmap_chart.title = 'Some Countries'
    worldmap_chart.add('F Countries', ['fr', 'fi'])
    worldmap_chart.add('M Countries', ['ma', 'mc', 'md', 'me', 'mg', 'mk', 'ml', 'mm', 'mn', 'mo', 'mr', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz'])
    worldmap_chart.add('U Countries', ['ua', 'ug', 'us', 'uy', 'uz'])
    path = f'{getcwd()}\\data\\test13-1.svg'
    worldmap_chart.render_to_file(path)
    open_new(path)

    supra = maps.world.SupranationalWorld()
    supra.title = 'World\'s Continents'
    supra.add('Asia', [('asia', 1)])
    supra.add('Europe', [('europe', 1)])
    supra.add('Africa', [('africa', 1)])
    supra.add('North america', [('north_america', 1)])
    supra.add('South america', [('south_america', 1)])
    supra.add('Oceania', [('oceania', 1)])
    supra.add('Antartica', [('antartica', 1)])
    path = f'{getcwd()}\\data\\test13-2.svg'
    supra.render_to_file(path)
    open_new(path)

def test14():
    fr_chart = maps.fr.Departments()
    fr_chart.title = 'Some Departments'
    fr_chart.add('Métropole', ['69', '92', '13'])
    fr_chart.add('Corse', ['2A', '2B'])
    fr_chart.add('DOM COM', ['971', '972', '973', '974'])
    path = f'{getcwd()}\\data\\test14-1.svg'
    fr_chart.render_to_file(path)
    open_new(path)

    fr_chart = maps.fr.Regions()
    fr_chart.title = 'Some Regions'
    fr_chart.add('Métropole', ['82', '11', '93'])
    fr_chart.add('Corse', ['94'])
    fr_chart.add('DOM COM', ['01', '02', '03', '04'])
    path = f'{getcwd()}\\data\\test14-2.svg'
    fr_chart.render_to_file(path)
    open_new(path)

def test15():
    ch_chart = maps.ch.Cantons()
    ch_chart.title = 'Some Cantons'
    ch_chart.add('Cantons 1', ['kt-zh', 'kt-be', 'kt-nw'])
    ch_chart.add('Cantons 2', ['kt-ow', 'kt-bs', 'kt-ne'])
    path = f'{getcwd()}\\data\\test15.svg'
    ch_chart.render_to_file(path)
    open_new(path)

def main_test():
    try:
        mkdir('data')
    except FileExistsError:
        pass

    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
    test11()
    test12()
    test13()
    test14()
    test15()

if __name__ == '__main__':
    main_test()
