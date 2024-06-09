import java.net.*;
import java.io.*;

class TCPClient {
    public static void main(String[] args) throws Exception {
        // Create a socket to connect to the server
        Socket sock = new Socket("127.0.0.1", 4000);

        // Get the filename from user input
        System.out.println("Enter the filename:");
        BufferedReader keyRead = new BufferedReader(new InputStreamReader(System.in));
        String fname = keyRead.readLine();

        // Get the output stream to send data to the server
        OutputStream ostream = sock.getOutputStream();
        PrintWriter pwrite = new PrintWriter(ostream, true);

        // Send the filename to the server
        pwrite.println(fname);

        // Get the input stream to receive data from the server
        InputStream istream = sock.getInputStream();
        BufferedReader socketRead = new BufferedReader(new InputStreamReader(istream));
        
        // Read and print data received from the server
        String str;
        while ((str = socketRead.readLine()) != null) {
            System.out.println(str);
        }

        // Close resources
        pwrite.close();
        socketRead.close();
        keyRead.close();
        sock.close();
    }
}
