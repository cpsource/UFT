A **graph** is a mathematical structure used to model relationships between objects. In its simplest form, a graph consists of a set of **nodes** (also called **vertices**) connected by **edges**.

### Key Concepts in Graphs

1. **Nodes (Vertices)**:
   - A **node** is a fundamental unit in a graph representing an object, entity, or point.
   - Each node can be connected to other nodes via edges.
   - Nodes can represent anything that needs to be connected in some way, like cities in a map, people in a social network, or webpages on the internet.

2. **Edges**:
   - An **edge** is a link or connection between two nodes.
   - Each edge represents a relationship or connection between the nodes it links.
   - Edges can be either **directed** or **undirected**:
     - **Undirected edges** have no direction; they connect nodes symmetrically (e.g., friendship in a social network where "A is friends with B" means "B is friends with A").
     - **Directed edges** have a direction, indicating a one-way relationship (e.g., following on Twitter, where "A follows B" doesn't mean "B follows A").

3. **Graph Types**:
   - **Undirected Graph**: All edges are undirected, and the relationships are mutual.
   - **Directed Graph (Digraph)**: All edges are directed, meaning each edge has a direction.
   - **Weighted Graph**: Each edge has a weight or cost, representing the "strength" or "cost" of the connection (e.g., distance between cities).
   - **Unweighted Graph**: All edges have equal importance, so they don’t carry weights.

### Visualizing a Graph

- **Nodes** are typically represented by circles or dots.
- **Edges** are drawn as lines or arrows connecting the nodes.
- The arrangement of nodes and edges doesn’t affect the structure, but it can make certain patterns easier to see.

### Applications of Graphs

Graphs are used in various fields to represent and analyze relationships:

- **Computer Networks**: Nodes represent computers or routers, and edges represent connections between them.
- **Social Networks**: Nodes represent individuals, and edges represent friendships or follower relationships.
- **Transportation**: Nodes represent locations (like airports or train stations), and edges represent routes.
- **Recommendation Systems**: Items and users are connected based on interests, forming a graph to suggest new content.

### Basic Terminology in Graphs

- **Path**: A sequence of edges connecting a series of nodes.
- **Degree of a Node**: The number of edges connected to a node.
- **Cycle**: A path that starts and ends at the same node without retracing any edge.

### Example

Consider a graph where:
- Nodes represent cities.
- Edges represent highways connecting those cities.

In this case:
- An undirected edge between City A and City B would indicate a two-way highway.
- A directed edge from City A to City B would indicate a one-way road from City A to City B.
  
In summary, graphs are powerful structures that let us represent complex networks of relationships through simple concepts: nodes (entities) and edges (relationships).
