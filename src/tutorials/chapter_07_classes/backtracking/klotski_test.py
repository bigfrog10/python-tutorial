
from tutorials.chapter_07_classes.backtracking.klotski import SlidingBlock, SlidingGameBoard, solve


# ## testing
def finish_criteria1(board):
    block = board.name_to_block['boss']
    return block.is_occupied(4, 1) and block.is_occupied(4, 2)


def test():
    # game1 = SlidingGameBoard(5, 4, [
    #     SlidingBlock('boss', 0, 1, 2, 2),
    #     SlidingBlock('general1', 2, 1, 1, 2),
    #     SlidingBlock('general2', 0, 0, 2, 1),
    # ], finish_criteria1)

    game1 = SlidingGameBoard(5, 4, [
        SlidingBlock('boss', 0, 1, 2, 2),

        SlidingBlock('general1', 2, 1, 1, 2),
        SlidingBlock('general2', 0, 0, 2, 1),
        SlidingBlock('general3', 0, 3, 2, 1),
        SlidingBlock('general4', 2, 0, 2, 1),
        SlidingBlock('general5', 2, 3, 2, 1),

        SlidingBlock('solder1', 3, 1, 1, 1),
        SlidingBlock('solder2', 3, 2, 1, 1),
        SlidingBlock('solder3', 4, 0, 1, 1),
        SlidingBlock('solder4', 4, 3, 1, 1),
    ], finish_criteria1)

    solution = solve(game1)
    for s in solution:
        print('-' * 80)
        print(len(s.steps))
        print(s)


# This is the plain run
# ##############################################################################
# test()

# This run provides how many calls it makes.
# ##############################################################################
import cProfile
cProfile.run('test()')

# This run provides tree view on calls
# ##############################################################################
# from pyinstrument import Profiler
#
# profiler = Profiler()
# profiler.start()
#
# test()
#
# profiler.stop()
# print(profiler.output_text(unicode=True, color=True))

# timing each line of a function
# ##############################################################################
# import line_profiler
# import atexit
# profile = line_profiler.LineProfiler()
# atexit.register(profile.print_stats)

# To time the top function
# ---------------------------------------------
# profile(test)()  # the way to wrap the function

# Or to time intermediate function. We don't want to modify existing code, so
# we inject aop here.
# ---------------------------------------------
# import tutorials.chapter_07_classes.backtracking.klotski as klotski
# klotski.move_to = profile(klotski.move_to)
# test()

# There are other tools we haven't tried yet:
#     https://docs.python.org/3/library/debug.html
#     https://github.com/vpelletier/pprofile
#     https://www.pyvmmonitor.com/

# There are also memory profilers:
#    https://github.com/pythonprofilers/memory_profiler
#    https://pythonhosted.org/Pympler/muppy.html
#    https://mg.pov.lt/objgraph/
