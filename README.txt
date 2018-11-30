createGraph.py must be ran with 6 arguments to initialize the inputs.
=====================================================================
The 6 arguments in order are:
Input size: s/ m/ l
Number of Vertices: 25-50/ 250-500/ 500-1000
Number of Edges: 300-1225/ 31125-124750/ 124750-499500
Number of Constraints: <100 / <1000 / <2000
Number of Buses: Any integer
Size of Buses: Any integer
=====================================================================
It can be ran from the command line in these simple forms.
=====================================================================
Here are the 3 examples used to create small, medium and large inputs.
Small: python createGraph.py s 25 50 10 4 8
Medium: python createGraph.py m 500 1000 40 20 30
Large: python createGraph.py l 800 2000 400 30 30

