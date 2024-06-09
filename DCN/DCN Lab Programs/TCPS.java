import java.net.*;
import java.io.*;

class TCPServer {
    public static void main(String[] args) throws Exception {
        // Create a server socket on port 4000
        ServerSocket sersock = new ServerSocket(4000);
        System.out.println("Server ready for connection");

        // Accept connection from a client
        Socket sock = sersock.accept();
        System.out.println("Connection is successful and waiting for chatting");

        // Get the input stream to receive data from the client
        InputStream istream = sock.getInputStream();
        BufferedReader fileRead = new BufferedReader(new InputStreamReader(istream));

        // Read the filename sent by the client
        String fname = fileRead.readLine();

        // Open the file and prepare to send its contents to the client
        BufferedReader contentRead = new BufferedReader(new FileReader(fname));
        OutputStream ostream = sock.getOutputStream();
        PrintWriter pwrite = new PrintWriter(ostream, true);

        // Read and send the contents of the file to the client
        String str;
        while ((str = contentRead.readLine()) != null) {
            pwrite.println(str);
        }

        // Close resources
        sock.close();
        sersock.close();
        pwrite.close();
        fileRead.close();
        contentRead.close();
    }
}
