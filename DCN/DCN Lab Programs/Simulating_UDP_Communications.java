import ns3.*;

public class FirstScriptExample {
    static {
        System.loadLibrary("ns3_core");
        System.loadLibrary("ns3_network");
        System.loadLibrary("ns3_internet");
        System.loadLibrary("ns3_point_to_point");
        System.loadLibrary("ns3_applications");
    }

    public static void main(String[] args) {
        // Set the time resolution to nanoseconds
        Time.SetResolution(Time.NS);
        
        // Enable logging for UdpEchoClientApplication and UdpEchoServerApplication
        LogComponentEnable("UdpEchoClientApplication", LogLevel.LOG_LEVEL_INFO);
        LogComponentEnable("UdpEchoServerApplication", LogLevel.LOG_LEVEL_INFO);

        // Create a container to hold two nodes
        NodeContainer nodes = new NodeContainer();
        nodes.Create(2);

        // Configure the point-to-point connection attributes
        PointToPointHelper pointToPoint = new PointToPointHelper();
        pointToPoint.SetDeviceAttribute("DataRate", StringValue.Value("5Mbps")); // Set data rate to 5 Mbps
        pointToPoint.SetChannelAttribute("Delay", StringValue.Value("2ms")); // Set delay to 2 milliseconds

        // Install the point-to-point devices onto the nodes
        NetDeviceContainer devices = pointToPoint.Install(nodes);

        // Install the internet stack on the nodes
        InternetStackHelper stack = new InternetStackHelper();
        stack.Install(nodes);

        // Assign IP addresses to the devices
        Ipv4AddressHelper address = new Ipv4AddressHelper();
        address.SetBase(Ipv4Address.Value("10.1.1.0"), Ipv4Mask.Value("255.255.255.0"));

        // Assign IP addresses to the devices
        Ipv4InterfaceContainer interfaces = address.Assign(devices);

        // Create a UdpEchoServer application on node 1, listening on port 9
        UdpEchoServerHelper echoServer = new UdpEchoServerHelper(9);

        // Install the UdpEchoServer application on node 1
        ApplicationContainer serverApps = echoServer.Install(nodes.Get(1));
        serverApps.Start(Seconds.Value(1.0)); // Start the server at 1 second
        serverApps.Stop(Seconds.Value(10.0)); // Stop the server at 10 seconds

        // Create a UdpEchoClient application to send data to the server's IP address and port
        UdpEchoClientHelper echoClient = new UdpEchoClientHelper(interfaces.GetAddress(1), 9);
        echoClient.SetAttribute("MaxPackets", UintegerValue.Value(1)); // Send only one packet
        echoClient.SetAttribute("Interval", TimeValue.Value(Seconds.Value(1.0))); // Interval between packets (1 second)
        echoClient.SetAttribute("PacketSize", UintegerValue.Value(1024)); // Packet size of 1024 bytes

        // Install the UdpEchoClient application on node 0
        ApplicationContainer clientApps = echoClient.Install(nodes.Get(0));
        clientApps.Start(Seconds.Value(2.0)); // Start the client at 2 seconds
        clientApps.Stop(Seconds.Value(10.0)); // Stop the client at 10 seconds

        // Run the simulation
        Simulator.Run();
        // Clean up and destroy the simulation
        Simulator.Destroy();
    }

    private static void LogComponentEnable(String component, int level) {
        // Method to enable logging for specific components
        LogComponentEnable(component, level);
    }

    private static void LogComponentEnable(String component, LogLevel level) {
        // Method to enable logging for specific components
        LogComponentEnable(component, level);
    }
}
