import java.util.Scanner;

public class LeakyBucket {
    public static void main(String[] args) {
        
        int a[] = new int[20]; // Array to store packet sizes
        int buck_rem = 0; // Remaining bucket capacity
        int buck_cap = 4; // Bucket capacity
        int rate = 3; // Transmission rate
        int sent, recv; // Variables to store sent and received packet sizes

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of packets:");
        int n = sc.nextInt(); // Number of packets
        System.out.println("Enter the packet_size of each packet:");
        for (int i = 1; i <= n; i++) {
            a[i] = sc.nextInt(); // Input packet sizes
        }

        System.out.println("Clock \t Packet Size \t Accept \t Sent \t Remaining");
        for (int i = 1; i <= n; i++) {
            // Receive packets
            if (a[i] != 0) {
                if (buck_rem + a[i] > buck_cap){
                    recv = -1;
                } // Packet dropped
                else{
                    recv = a[i];
                    buck_rem += a[i]; // Update remaining bucket capacity
                 } // Packet received
            }
            else {
                recv = 0; // No packet received
            }

            // Send packets
            if (buck_rem != 0) {
                if (buck_rem < rate) {
                    sent = buck_rem; // Send remaining packets
                    buck_rem = 0; // Bucket becomes empty
                }
                else {
                    sent = rate; // Send packets at rate
                    buck_rem -= rate; // Update remaining bucket capacity
                }
            }
            else {
                sent = 0; // No packets sent
            }

            // Display information
            if (recv == -1) {
                System.out.println(i + "\t\t" + a[i] + "\t Dropped \t" + sent + "\t" + buck_rem);
            }
            else {
                System.out.println(i + "\t\t" + a[i] + "\t\t" + recv + "\t" + sent + "\t" + buck_rem);
            }
        }
    }
}
