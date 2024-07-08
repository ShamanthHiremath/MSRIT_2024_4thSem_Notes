import java.util.Arrays;
import java.util.Scanner;

public class BellmanFord {

    public static int[] bellmanFord(int n, int m, int src, int[][] edges) {
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;

        // Relax edges for n-1 iterations
        for (int i = 0; i < n - 1; i++) {
            for (int[] edge : edges) {
                int u = edge[0];
                int v = edge[1];
                int weight = edge[2];
                if (dist[u] != Integer.MAX_VALUE && dist[v] > dist[u] + weight ) {
                    dist[v] = dist[u] + weight;
                }
            }
        }

        // Check for negative cycles
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int weight = edge[2];
            if (dist[u] != Integer.MAX_VALUE && dist[u] + weight < dist[v]) {
                // Negative cycle detected
                return new int[]{0}; // Returning an array with a single element to indicate negative cycle
            }
        }

        return dist;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of vertices: ");
        int n = scanner.nextInt();

        System.out.print("Enter the number of edges: ");
        int m = scanner.nextInt();

        int[][] edges = new int[m][3];

        System.out.println("Enter the edges in the format 'source destination weight':");
        for (int i = 0; i < m; i++) {
            System.out.print("Edge " + (i + 1) + ": ");
            edges[i][0] = scanner.nextInt();
            edges[i][1] = scanner.nextInt();
            edges[i][2] = scanner.nextInt();
        }

        System.out.print("Enter the source vertex: ");
        int src = scanner.nextInt();

        int[] shortestDistances = bellmanFord(n, m, src, edges);

        // Output the shortest distances from the source vertex
        for (int i = 0; i < n; i++) {
            System.out.print("Distance to vertex " + i + " from source " + src + ": ");
            if (shortestDistances[i] == Integer.MAX_VALUE) {
                System.out.println("Infinity");
            } else {
                System.out.println(shortestDistances[i]);
            }
        }

        scanner.close();
    }
}
