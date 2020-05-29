# DAG operations
 Finding ancestors and descendants of elements of a DAG and checking if given trail is a path

### Methodology:
1. Number of nodes are taken as input
2. 1 to N unique nodes are generated
3. Number of edges is taken as input
4. N edges are taken as input
5. A dictionary of the network is created with key being the node and the value being a list of nodes to which the current node directs edges to.

>isTrailPath() Function returns a Boolean value which states if the given trail was a path or not.
>findAncestories() function computes descendants recursively. The descendants are then used to compute the ancestors.
>makeGraph() inputs values and returns a network graph.

### Assumptions:
1. Node ids are integers
2. Only DAGs are given as input, i.e. no cycles exist.
3. All edges are directed
4. Trails are atleast 2 nodes long.

