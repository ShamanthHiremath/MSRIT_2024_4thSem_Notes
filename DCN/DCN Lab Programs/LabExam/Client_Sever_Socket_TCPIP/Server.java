// 6) A. Write a client-server program using TCP/IP sockets in which client requests for a file by
// sending the file name to the server, and the server sends back the contents of the requested
// file if present

import java.net.*;
import java.io.*;

public class Server {
    public static void main(String[] args) throws Exception {

        ServerSocket sersock = new ServerSocket(4000);
        System.out.println("Server ready for connection");

        Socket sock = sersock.accept();
        System.out.println("Connection Is successful and waiting for chatting");

        InputStream istream = sock.getInputStream();
        BufferedReader fileRead = new BufferedReader(new InputStreamReader(istream));
        String fname = fileRead.readLine();

        
        OutputStream ostream = sock.getOutputStream();
        PrintWriter pwrite = new PrintWriter(ostream, true);

        BufferedReader ContentRead = new BufferedReader(new FileReader(fname));
        String str;
        while ((str = ContentRead.readLine()) != null) {
            pwrite.println(str);
        }
        
        sock.close();
        sersock.close();
        pwrite.close();
        fileRead.close();
        ContentRead.close();
    }
}