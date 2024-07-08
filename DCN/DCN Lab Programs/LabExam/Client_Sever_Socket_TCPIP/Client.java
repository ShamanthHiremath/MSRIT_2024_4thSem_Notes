// 6) A. Write a client-server program using TCP/IP sockets in which client requests for a file by
// sending the file name to the server, and the server sends back the contents of the requested
// file if present

import java.net.*;
import java.io.*;

public class Client {
    public static void main(String[] args) throws Exception {

        Socket sock = new Socket("127.0.0.1", 4000);
        
        System.out.println("Enter the filename");
        BufferedReader keyRead = new BufferedReader(new InputStreamReader(System.in));
        String fname = keyRead.readLine();

        OutputStream ostream = sock.getOutputStream();
        PrintWriter pwrite = new PrintWriter(ostream, true);
        pwrite.println(fname);
        
        InputStream istream = sock.getInputStream();
        BufferedReader socketRead = new BufferedReader(new InputStreamReader(istream));
        String str;
        while ((str = socketRead.readLine()) != null) {
            System.out.println(str);
        }
        
        pwrite.close();
        socketRead.close();
        keyRead.close();
        sock.close();
    }
}