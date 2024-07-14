import java.util.Scanner;

public class TDMSimulator {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of stations (maximum 10): ");
        int numberOfStations = sc.nextInt();

        int[] processingTime = new int[numberOfStations]; // Processing time for each station
        int[] waitingTime = new int[numberOfStations]; // Waiting time for each station
        int[] turnaroundTime = new int[numberOfStations]; // Turnaround time for each station
        int[] remainingTime = new int[numberOfStations]; // Remaining processing time for each station

        System.out.println("Enter the processing time for each station:");
        for (int i = 0; i < numberOfStations; i++) {
            System.out.print("Station " + (i + 1) + ": ");
            processingTime[i] = sc.nextInt();
            remainingTime[i] = processingTime[i];
        }

        System.out.print("Enter the frame size: ");
        int frameSize = sc.nextInt(); // Frame size

        int currentTime = 0; // Current time
        while (true) {
            boolean allStationsDone = true;

            for (int i = 0; i < numberOfStations; i++) {
                if (remainingTime[i] > 0) {
                    allStationsDone = false;

                    if (remainingTime[i] > frameSize) {
                        currentTime += frameSize;
                        remainingTime[i] -= frameSize;
                    } else {
                        currentTime += remainingTime[i];
                        remainingTime[i] = 0;
                        turnaroundTime[i] = currentTime;
                    }
                }
            }

            if (allStationsDone) break;
        }

        float totalWaitingTime = 0, totalTurnaroundTime = 0;

        System.out.println("----------------------------------------------------------");
        System.out.println("Station\tProcessing Time\tCompletion Time\tWaiting Time");
        System.out.println("----------------------------------------------------------");

        for (int i = 0; i < numberOfStations; i++) {
            waitingTime[i] = turnaroundTime[i] - processingTime[i];
            totalWaitingTime += waitingTime[i];
            totalTurnaroundTime += turnaroundTime[i];

            System.out.println((i + 1) + "\t\t" + processingTime[i] + "\t\t" + turnaroundTime[i] + "\t\t" + waitingTime[i]);
        }

        float averageWaitingTime = totalWaitingTime / numberOfStations;
        float averageTurnaroundTime = totalTurnaroundTime / numberOfStations;

        System.out.println("----------------------------------------------------------");
        System.out.println("Average Waiting Time: " + averageWaitingTime);
        System.out.println("Average Turnaround Time: " + averageTurnaroundTime);
    }
}
