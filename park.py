from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(set)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].add(to_node)
        self.distances[(from_node, to_node)] = distance

    def __repr__(self):
        return 'Graph = > nodes: {}, edges: {}, distances: {}'.format(self.nodes, self.edges, self.distances)


class Route:
    def __init__(self, route):
        self.route = route
        self.visited = set(self.route)
        self.last_visited = self.route[-1]


class ReccomendEngine:
    def __init__(self, filename='example'):
        self.places = 0
        self.people = 0
        self.graph = Graph()
        self.test_man = None
        self.rating = []
        self.filename = filename
        self.rating_weight = 0.4

    def _parse_file(self, filename):
        with open(filename, 'r') as f:
            file_input = f.readlines()

        entries = []
        for line in file_input:
            entries.append([int(i) for i in line.split()])

        return entries

    def _make_graph(self, data):
        for entry in data:
            self.graph.add_node(entry[0])
            for n, node in enumerate(entry[2:]):
                if n == entry[0]:
                    next
                self.graph.add_edge(n, entry[0], node)

    def _make_ratings(self, data):
        for entry in data:
            for i in entry:
                self.rating[i] += 1
        self.rating = [r / self.people for r in self.rating]

    def handle_file(self, name=None):
        filename = name or self.filename

        entries = self._parse_file(filename)
        self.places = entries[0][0]
        self._make_graph(entries[1:self.places + 1])
        self.rating = [0] * self.places
        self.people = entries[self.places + 1][0]
        self._make_ratings(entries[self.places + 2:-1])
        self.test_man = Route(entries[-1])

    def handle_input(self):
        self.places = int(input('Number of places: '))
        for i in range(self.places):
            entry = [int(e) for e in input(
                'Place entry: <Place Number> <Place Type> [<distance to place N>] : Repeated N times ').split()]

            self.graph.add_node(entry[0])
            for i, node in enumerate(entry[2:]):
                if i == entry[0]:
                    next
                self.graph.add_edge(i, entry[0], node)
        self.rating = [0] * self.places
        self.people = int(input('Number of people s routes: '))

        for i in range(self.people):
            entry = [int(e) for e in input('[<Place Number>]+ ').split()]
            for i in entry:
                self.rating[i] += 1
        self.rating = [r / self.people for r in self.rating]
        self.test_man = Route([int(e) for e in input('Current Route: ').split()])

    def _make_map(self, places, test_man):
        map = []
        for i in places:
            map.append((i, self.graph.distances[(test_man.last_visited, i)], self.rating[i]))
        return map

    def reccommend(self, test_man=None):
        test_man = Route(test_man) if test_man else self.test_man
        places = list(self.graph.edges[test_man.last_visited] - set(test_man.visited))
        return self._make_map(places, test_man)

    def reccomend_by_distance(self, test_man=None, pretty=False):
        map = self.reccommend(test_man)
        if pretty:
            return [i[0] for i in sorted(map, key=lambda x: x[1])[:5]]
        return sorted(map, key=lambda x: x[1])[:5]

    def reccomend_by_distance_ratings(self, test_man=None, pretty=False):
        map = self.reccommend(test_man)
        if pretty:
            return [i[0] for i in sorted(map, key=lambda x: x[1] * self.rating_weight * x[2], reverse=True)[:5]]
        return sorted(map, key=lambda x: x[1] * self.rating_weight * x[2], reverse=True)[:5]


if __name__ == '__main__':
    re = ReccomendEngine()
    print('Using input mode')
    re.handle_input()
    print('Reccomendation by distance')
    print(re.reccomend_by_distance(pretty=True))
    print('Reccomendation by distance and rating')
    print(re.reccomend_by_distance_ratings(pretty=True))

    print('Using file sample mode')
    re.handle_file()
    print('Reccomendation by distance')
    print(re.reccomend_by_distance())
    print('Reccomendation by distance and rating')
    print(re.reccomend_by_distance_ratings())
