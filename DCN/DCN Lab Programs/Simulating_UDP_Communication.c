#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"

using namespace ns3;

// Define a log component for this script
NS_LOG_COMPONENT_DEFINE ("FirstScriptExample");

int main (int argc, char *argv[])
{
  // Set the time resolution to nanoseconds
  Time::SetResolution (Time::NS);
  // Enable logging for UdpEchoClient and UdpEchoServer applications
  LogComponentEnable ("UdpEchoClientApplication", LOG_LEVEL_INFO);
  LogComponentEnable ("UdpEchoServerApplication", LOG_LEVEL_INFO);

  // Create a container to hold two nodes
  NodeContainer nodes;
  nodes.Create (2);

  // Configure the point-to-point connection attributes
  PointToPointHelper pointToPoint;
  pointToPoint.SetDeviceAttribute ("DataRate", StringValue ("5Mbps")); // Set data rate to 5 Mbps
  pointToPoint.SetChannelAttribute ("Delay", StringValue ("2ms")); // Set delay to 2 milliseconds

  // Install the point-to-point devices onto the nodes
  NetDeviceContainer devices;
  devices = pointToPoint.Install (nodes);

  // Install the internet stack on the nodes
  InternetStackHelper stack;
  stack.Install (nodes);

  // Assign IP addresses to the devices
  Ipv4AddressHelper address;
  address.SetBase ("10.1.1.0", "255.255.255.0");

  // Assign IP addresses to the devices
  Ipv4InterfaceContainer interfaces = address.Assign (devices);

  // Create a UdpEchoServer application on node 1, listening on port 9
  UdpEchoServerHelper echoServer (9);

  // Install the UdpEchoServer application on node 1
  ApplicationContainer serverApps = echoServer.Install (nodes.Get (1));
  serverApps.Start (Seconds (1.0)); // Start the server at 1 second
  serverApps.Stop (Seconds (10.0)); // Stop the server at 10 seconds

  // Create a UdpEchoClient application to send data to the server's IP address and port
  UdpEchoClientHelper echoClient (interfaces.GetAddress (1), 9);
  echoClient.SetAttribute ("MaxPackets", UintegerValue (1)); // Send only one packet
  echoClient.SetAttribute ("Interval", TimeValue (Seconds (1.0))); // Interval between packets (1 second)
  echoClient.SetAttribute ("PacketSize", UintegerValue (1024)); // Packet size of 1024 bytes

  // Install the UdpEchoClient application on node 0
  ApplicationContainer clientApps = echoClient.Install (nodes.Get (0));
  clientApps.Start (Seconds (2.0)); // Start the client at 2 seconds
  clientApps.Stop (Seconds (10.0)); // Stop the client at 10 seconds

  // Run the simulation
  Simulator::Run ();
  // Clean up and destroy the simulation
  Simulator::Destroy ();
  return 0;
}