class Board:
    """ The Board class represents the low-level physical configuration of the 
        8-puzzle game. """

    # The 8-puzzle board can be represented as a list of length 8
    def __init__(self, initial_values=[]):
        self.value = initial_values

    def __eq__(self, other): 
        return self.value == other.value

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        return hash(str(self))

    # If 0 is in the top most block, then up is invalid
    def up(self):
        pos = self.value.index(0)
        if pos in (0, 1, 2):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos-3] = new_val[pos-3], new_val[pos]
            return new_val

    # If 0 is in the bottom most block, then up is invalid
    def down(self):
        pos = self.value.index(0)
        if pos in (6, 7, 8):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos+3] = new_val[pos+3], new_val[pos]
            return new_val

    # If 0 is in the left most block, then up is invalid
    def left(self):
        pos = self.value.index(0)
        if pos in (0, 3, 6):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos-1] = new_val[pos-1], new_val[pos]
            return new_val

    # If 0 is in the right most block, then up is invalid
    def right(self):
        pos = self.value.index(0)
        if pos in (2, 5, 8):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos+1] = new_val[pos+1], new_val[pos]
            return new_val



class State:
    """ Handles the state of the game """

    def __init__(self, initial_state=[]):
        self.current = Board(initial_state)

    def __eq__(self, other): 
        return self.current == other.current

    def __str__(self):
        return str(self.current)

    def __hash__(self):
        return hash(str(self))

    def up(self):
        up = self.current.up()
        if up is not None:
            return State(up)
        else:
            return self

    def down(self):
        down = self.current.down()
        if down is not None:
            return State(down)
        else:
            return self

    def left(self):
        left = self.current.left()
        if left is not None:
            return State(left)
        else:
            return self

    def right(self):
        right = self.current.right()
        if right is not None:
            return State(right)
        else:
            return self

    def successors(self):
        succ = []

        up = self.current.up()
        if up != None:
            succ.append(State(up))


        down = self.current.down()
        if down != None:
            succ.append(State(down))


        left = self.current.left()
        if left != None:
            succ.append(State(left))


        right = self.current.right()
        if right != None:
            succ.append(State(right))

        return succ




def goal_test(state):
    return str(state) == str(range(0, 9))


# BFS Search
def bfs(start):
    """ 
    Performs breadth-first search starting with the 'start' as the beginning
    node. Returns a namedtuple 'Success' which contains namedtuple 'position'
    (includes: node, cost, depth, prev), 'max_depth' and 'nodes_expanded'
    if a node that passes the goal test has been found.

    """

    # SearchPos used for bookeeping and finding the path:
    SearchPos = namedtuple('SearchPos', 'node, cost, depth, prev')

    # Initial position does not have a predecessor
    position = SearchPos(start, 0, 0, None)


    # frontier contains unexpanded positions
    frontier = [position]
    explored = set()
    while len(frontier) > 0:

        # current position is the first position in the frontier
        position = frontier.pop(0)

        node = position.node

        # goal test: return success if True
        if goal_test(node):
            max_depth = max([pos.depth for pos in frontier])
            Success = namedtuple('Success', 
                        'position, max_depth, nodes_expanded')
            success = Success(position, max_depth, len(explored))
            return success

        # expanded nodes are added to explored set
        explored.add(node)

        # All reachable positions from current postion is added to frontier
        for neighbor in node.successors():
            new_position = SearchPos(neighbor, position.cost + 1,
                                    position.depth + 1, position)
            frontier_check = neighbor in [pos.node for pos in frontier]
            if neighbor not in explored and not frontier_check:
                frontier.append(new_position)

    # the goal could not be reached.
    return None


import time



def trace_path(last_pos):
    pos = last_pos.prev
    next_pos = last_pos

    path = []

    while pos != None:
        if pos.node.up() == next_pos.node:
            path.append("Up")
        elif pos.node.down() == next_pos.node:
            path.append("Down")
        elif pos.node.left() == next_pos.node:
            path.append("Left")
        elif pos.node.right() == next_pos.node:
            path.append("Right")

        pos = pos.prev
        next_pos = next_pos.prev

    return path[::-1]


start_time = time.time()
config = [1,2,5,3,4,0,6,7,8]

game = State(config)

result = search.bfs(game)
final_pos = result.position
max_depth = result.max_depth
nodes_expanded = result.nodes_expanded

print "path_to_goal:", trace_path(final_pos)
print "cost_of_path:", final_pos.cost
print "nodes_expanded:", nodes_expanded
print "search_depth:", final_pos.depth
print "max_search_depth:", max_depth
print "running_time:", time.time() - start_time
print "max_ram_usage", resource.getrusage(1)[2]