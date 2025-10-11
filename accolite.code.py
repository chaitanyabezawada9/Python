"""NOTE Please switch to explorer tab and follow the folder structure to write the code 
PROBLEM: Festival of Spirits Eywa's Festival 
	In the mystical world of Pandora, the Na'vi tribes live in harmony with the life force of Eywa. They have N sacred sites, numbered from O to N-1, connected by pathways with the Great Tree at site Ø at the center. When new sacred sites are discovered, they are added to this network, favoring a connection to the left. If the left is occupied, they connect to the right instead. The Na'vi keep track of the number of guardians at each site in the Book of Souls. Outp No Ou For the upcoming Eywa Festival, the Na'vi need to choose the perfect site for the celebration. They use a special number, M, to determine this site through a specific traversal of the network. This hallowed traversal respects the order of connecting to the left first, then the site itself, and finally the right. The chosen Mth site, revealed through this hallowed traversal, will host the festival, its guardian count ensuring a gathering resonant with Eywa's energy and peace. Write an algorithm to find the number of Na'vi guardians at choosen sacred site. 

	Input: Enter an integer N(i.e number of sacred sites) and put semi-colon then enter N space-separated integers representing the number of Na'vi guardians at each sacred site. Then put semi-colon and enter two space-separated integers pathwayCount and connectionCount(will always be 2). Then put semi-colon and enter pathwayCount set seperated by semi-colon consisting of connectionCount space-separated integers, representing the sacred sites connected by an energy pathway.Then enter semi-colon and enter an integer M. 

	For Example:\n7;10 20 15 25 30 18 22;6 2:0 1:0 2:1 3;1 4;25;2 6;3 C No Output Print an integer representing the number of Na'vi guardians at choosen sacred site. Constraints 0 <= siteCount <= 10^4 0< 1 2 siteGuardians[0], siteGuardians [1],......, siter 3 1] < 10^4 0< festivalsite <= siteCount Example Input: 7;10 20 15 25 30 18 22;6 2;0 1;0 2;1 3;1 4;2 5;2 6;3 

	Output: 30 

	Explanation: 

    The hierarchy is as given below: 0 1 2 /\/\ 3 4 5 6 Outp No Out As per the given rule, the generated sequence of sacred sites is 3,1,4,0,5,2,6. Now the Mth (3rd as M-3) sacred site has Number: 4 The count of guardinas at the sacred site number 4 is 30. So, the output is 30."""



  #code
# Read input
inp = input().strip()
parts = inp.split(';')

# Number of sacred sites and guardians
N = int(parts[0])
guardians = list(map(int, parts[1].split()))

# Pathway info
pathway_info = parts[2].split()
pathwayCount = int(pathway_info[0])

# Pathways (edges)
edges = []
for e in parts[3:3+pathwayCount]:
    edges.append(list(map(int, e.split())))

# Mth site
M = int(parts[3 + pathwayCount])

# Build tree as adjacency list (left-first, then right)
tree = {i: [] for i in range(N)}
children = set()
for u, v in edges:
    tree[u].append(v)
    children.add(v)

# Root node
root_candidates = set(range(N)) - children
root = root_candidates.pop()

# Step 1: Compute subtree sizes using DP
subtree_size = [0]*N

def compute_size(node):
    size = 1
    for child in tree[node]:
        size += compute_size(child)
    subtree_size[node] = size
    return size

compute_size(root)

# Step 2: Find M-th node using subtree sizes
def find_mth(node, m):
    left_size = subtree_size[tree[node][0]] if len(tree[node]) >= 1 else 0
    if m <= left_size:
        return find_mth(tree[node][0], m)
    elif m == left_size + 1:
        return node
    else:
        if len(tree[node]) == 2:
            return find_mth(tree[node][1], m - left_size - 1)
        else:
            return None

chosen_site = find_mth(root, M)
print(guardians[chosen_site])

