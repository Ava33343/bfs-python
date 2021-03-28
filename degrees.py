import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    # TODO
    
    
    
    
    
    
    
#    graph = {
#      'A' : ['B','C'],
#      'B' : ['D', 'E'],
#      'C' : ['F'],
#      'D' : [],
#      'E' : ['F'],
#      'F' : []
#        }
#
#        visited = [] # List to keep track of visited nodes.
#        queue = []     #Initialize a queue
#
#        def bfs(visited, graph, node):
#          visited.append(node)
#          queue.append(node)
#
#          while queue:
#            s = queue.pop(0)
#            print (s, end = " ")
#
#            for neighbour in graph[s]:
#              if neighbour not in visited:
#                visited.append(neighbour)
#                queue.append(neighbour)

#            # Driver Code
#            bfs(visited, graph, 'A')
#                raise NotImplementedError
'''
# https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python

Explanation
Lines 3-10: The illustrated graph is represented using an adjacency list. An easy way to do this in Python is to use a dictionary data structure, where each vertex has a stored list of its adjacent nodes.

Line 12: visited is a list that is used to keep track of visited nodes.

Line 13: queue is a list that is used to keep track of nodes currently in the queue.

Line 29: The arguments of the bfs function are the visited list, the graph in the form of a dictionary, and the starting node A.

Lines 15-26: bfs follows the algorithm described above:

It checks and appends the starting node to the visited list and the queue.
Then, while the queue contains elements, it keeps taking out nodes from the queue, appends the neighbors of that node to the queue if they are unvisited, and marks them as visited.
This continues until the queue is empty.
Time Complexity
Since all of ​the nodes and vertices are visited, the time complexity for BFS on a graph is O(V + E)O(V+E); where VV is the number of vertices and EE is the number of edges.
'''

'''
http://www.acme.byu.edu/wp-content/uploads/2016/09/Vol2A-BFS-2016.pdf
'''

'''
https://stackoverflow.com/questions/47586428/shortest-path-graph-traversal-for-kevin-bacon-game/47623977

def bfs(self, actor):
    from heapq import heappush, heappop
    if actor == "Kevin Bacon":
        return print("This actor is Kevin Bacon!")
    visited = set()
    checked = []
    n = 0
    heappush(checked, (0, n, [self.get_vertex(actor)]))
    # if the list is empty we haven't been able to find any path
    while checked:
        # note that we pop our current list out of the list of checked lists,
        # if all of the children of this list have been visited it won't be
        # added again
        current_list = heappop(checked)[2]
        current_vertex = current_list[-1]
        if current_vertex.ID == "Kevin Bacon":
            return print(current_list)
        for child in current_vertex.get_connections():
            if child in visited:
                # we've already found a shorter path to this actor
                # don't add this path into the list
                continue
            n += 1
            # make a hash function for the vertexes, probably just
            # the hash of the ID is enough, ptherwise the memory address
            # is used and identical vertices can be visited multiple times
            visited.add(child)
            w = sum(current_list[i].get_weight(current_list[i+1])
                    for i in range(len(current_list)-1))
            heappush(checked, (w, n, current_list + [child]))
    print("no path found!")
    
    # You should also implement a __repr__() method for your vertex class. With the one I used, the output looks like this:
    
    g = Graph()
        for t in [("Kevin Bacon", "actor1", "movie1")
        ,("Kevin Bacon", "actor2", "movie1")
        ,("actor1", "actor2", "movie1")
        ,("actor1", "actor3", "movie2")
        ,("actor3", "actor2", "movie3")
        ,("actor3", "actor4", "movie4")
        ,("actor5", "actor6", "movie5")]:
            g.add_edge(t[0],t[1],cost=1)
            g.add_edge(t[1],t[0],cost=1)

        g.bfs("actor4")
        # prints [Vertex(actor4), Vertex(actor3), Vertex(actor2), Vertex(Kevin Bacon)]
            
'''

def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
