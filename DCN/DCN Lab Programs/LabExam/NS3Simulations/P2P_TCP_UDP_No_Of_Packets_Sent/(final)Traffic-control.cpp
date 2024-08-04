/*
***************************************************************************************************
4) B.
14) B.

Simulate a four node point-to-point network, and connect the links as follows: n0-n2, n1-n2 and 
n2-n3. Apply TCP agent between n0-n3 and UDP agent between n1-n3. Apply relevant
applications over TCP and UDP agents by changing the parameters and determine the
number of packets sent by TCP/UDP.
*/

/*
 * Copyright (c) 2015 Universita' degli Studi di Napoli "Federico II"
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 * Author: Pasquale Imputato <p.imputato@gmail.com>
 * Author: Stefano Avallone <stefano.avallone@unina.it>
 */

#include "ns3/applications-module.h"
#include "ns3/core-module.h"
#include "ns3/flow-monitor-module.h"
#include "ns3/internet-module.h"
#include "ns3/network-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/traffic-control-module.h"

// This simple example shows how to use TrafficControlHelper to install a
// QueueDisc on a device.
//
// The default QueueDisc is a pfifo_fast with a capacity of 1000 packets (as in
// Linux). However, in this example, we install a RedQueueDisc with a capacity
// of 10000 packets.
//
// Network topology
//
//       10.1.1.0
// n0 -------------- n1
//    point-to-point
//
// The output will consist of all the traced changes in the length of the RED
// internal queue and in the length of the netdevice queue:
//
//    DevicePacketsInQueue 0 to 1
//    TcPacketsInQueue 7 to 8
//    TcPacketsInQueue 8 to 9
//    DevicePacketsInQueue 1 to 0
//    TcPacketsInQueue 9 to 8
//
// plus some statistics collected at the network layer (by the flow monitor)
// and the application layer. Finally, the number of packets dropped by the
// queuing discipline, the number of packets dropped by the netdevice and
// the number of packets requeued by the queuing discipline are reported.
//
// If the size of the DropTail queue of the netdevice were increased from 1
// to a large number (e.g. 1000), one would observe that the number of dropped
// packets goes to zero, but the latency grows in an uncontrolled manner. This
// is the so-called bufferbloat problem, and illustrates the importance of
// having a small device queue, so that the standing queues build in the traffic
// control layer where they can be managed by advanced queue discs rather than
// in the device layer.

using namespace ns3;

// 1. **********************************
// Comment the following lines


// NS_LOG_COMPONENT_DEFINE("TrafficControlExample");

// /**
//  * Number of packets in TX queue trace.
//  *
//  * \param oldValue Old velue.
//  * \param newValue New value.
//  */
// void
// TcPacketsInQueueTrace(uint32_t oldValue, uint32_t newValue)
// {
//     std::cout << "TcPacketsInQueue " << oldValue << " to " << newValue << std::endl;
// }

// /**
//  * Packets in the device queue trace.
//  *
//  * \param oldValue Old velue.
//  * \param newValue New value.
//  */
// void
// DevicePacketsInQueueTrace(uint32_t oldValue, uint32_t newValue)
// {
//     std::cout << "DevicePacketsInQueue " << oldValue << " to " << newValue << std::endl;
// }

// /**
//  * TC Soujoun time trace.
//  *
//  * \param sojournTime The soujourn time.
//  */
// void
// SojournTimeTrace(Time sojournTime)
// {
//     std::cout << "Sojourn time " << sojournTime.ToDouble(Time::MS) << "ms" << std::endl;
// }


int
main(int argc, char* argv[])
{
    double simulationTime = 10; // seconds

// 2. **********************************
// Comment following two lines
    // std::string transportProt = "Tcp";
    // std::string socketType;

    CommandLine cmd(__FILE__);
// 3. **********************************
// Comment the following line
    // cmd.AddValue("transportProt", "Transport protocol to use: Tcp, Udp", transportProt);
    cmd.Parse(argc, argv);

// 4. **********************************
// Comment the following block
    // if (transportProt == "Tcp")
    // {
    //     socketType = "ns3::TcpSocketFactory";
    // }
    // else
    // {
    //     socketType = "ns3::UdpSocketFactory";
    // }

    NodeContainer nodes;
// 5. **********************************
// Change the number of nodes from 2 to 4
    nodes.Create(4);

    PointToPointHelper pointToPoint;
    pointToPoint.SetDeviceAttribute("DataRate", StringValue("10Mbps"));
    pointToPoint.SetChannelAttribute("Delay", StringValue("2ms"));
    pointToPoint.SetQueue("ns3::DropTailQueue", "MaxSize", StringValue("1p"));

// 6. **********************************
// Comment the following two lines
    // NetDeviceContainer devices;
    // devices = pointToPoint.Install(nodes);

    InternetStackHelper stack;
    stack.Install(nodes);

// 7. **********************************
// Comment the following block
    // TrafficControlHelper tch;
    // tch.SetRootQueueDisc("ns3::RedQueueDisc");
    // QueueDiscContainer qdiscs = tch.Install(devices);

    // Ptr<QueueDisc> q = qdiscs.Get(1);
    // q->TraceConnectWithoutContext("PacketsInQueue", MakeCallback(&TcPacketsInQueueTrace));
    // Config::ConnectWithoutContext(
    //     "/NodeList/1/$ns3::TrafficControlLayer/RootQueueDiscList/0/SojournTime",
    //     MakeCallback(&SojournTimeTrace));

    // Ptr<NetDevice> nd = devices.Get(1);
    // Ptr<PointToPointNetDevice> ptpnd = DynamicCast<PointToPointNetDevice>(nd);
    // Ptr<Queue<Packet>> queue = ptpnd->GetQueue();
    // queue->TraceConnectWithoutContext("PacketsInQueue", MakeCallback(&DevicePacketsInQueueTrace));

// For UDP **********************************

    Ipv4AddressHelper address;
    address.SetBase("10.1.1.0", "255.255.255.0");
//8. **********************************
// Copy 6th comment and change nodes -> nodes.Get(0), nodes.Get(1)
    NetDeviceContainer devices;
    devices = pointToPoint.Install(nodes.Get(0),nodes.Get(1));
    Ipv4InterfaceContainer interfaces = address.Assign(devices);

// 9. **********************************
// Add the following 3 lines devices, address, interfaces
    devices = pointToPoint.Install (nodes.Get (1), nodes.Get (2));
    address.SetBase ("10.1.2.0", "255.255.255.0");
    interfaces = address.Assign (devices);

// For TCP **********************************


// 10. **********************************
// Copy above 8 lines and do necessary changes
    Ipv4AddressHelper address1;
    address1.SetBase("10.1.3.0", "255.255.255.0");

    NetDeviceContainer devices1;
    devices1 = pointToPoint.Install(nodes.Get(3),nodes.Get(1));
    Ipv4InterfaceContainer interfaces1 = address1.Assign(devices1);

    devices1 = pointToPoint.Install (nodes.Get (1), nodes.Get (2));
    address1.SetBase ("10.1.4.0", "255.255.255.0");
    interfaces1 = address1.Assign (devices1);

// 11. **********************************
// Add this line from third.cc(line 173)
    Ipv4GlobalRoutingHelper::PopulateRoutingTables ();

// For UDP **********************************

    // Flow
    uint16_t port = 7;
    Address localAddress(InetSocketAddress(Ipv4Address::GetAny(), port));
// 12. **********************************
// change all socketType to "ns3::UdpSocketFactory"
    PacketSinkHelper packetSinkHelper("ns3::UdpSocketFactory", localAddress);
// 13. **********************************
// Change nodes.Get(0) -> nodes.Get(2)
    ApplicationContainer sinkApp = packetSinkHelper.Install(nodes.Get(2));

    sinkApp.Start(Seconds(0.0));
    sinkApp.Stop(Seconds(simulationTime + 0.1));

    uint32_t payloadSize = 1448;

    Config::SetDefault("ns3::TcpSocket::SegmentSize", UintegerValue(payloadSize));

    OnOffHelper onoff("ns3::UdpSocketFactory", Ipv4Address::GetAny());
    onoff.SetAttribute("OnTime", StringValue("ns3::ConstantRandomVariable[Constant=1]"));
    onoff.SetAttribute("OffTime", StringValue("ns3::ConstantRandomVariable[Constant=0]"));
    onoff.SetAttribute("PacketSize", UintegerValue(payloadSize));
    onoff.SetAttribute("DataRate", StringValue("50Mbps")); // bit/s
    ApplicationContainer apps;
//14. **********************************
// Change interfaces.GetAddress(0) -> interfaces.GetAddress(1)
    InetSocketAddress rmt(interfaces.GetAddress(1), port);
    rmt.SetTos(0xb8);
    AddressValue remoteAddress(rmt);
    onoff.SetAttribute("Remote", remoteAddress);
// 15. **********************************
// Change nodes.Get(1) -> nodes.Get(0)
    apps.Add(onoff.Install(nodes.Get(0)));
    apps.Start(Seconds(1.0));
    apps.Stop(Seconds(simulationTime + 0.1));

// For TCP **********************************

// 16. **********************************
// Copy the above Flow block starting from uint16_t till apps.Stop()
// 17. **********************************
// Change port -> port1 and set 7 -> 9, replace all port -> port1
// Change localAddress to localAddress1
     uint16_t port1 = 9;
    Address localAddress1(InetSocketAddress(Ipv4Address::GetAny(), port1));
// 18. **********************************
// Replace all "ns3::UdpSocketFactory" -> "ns3::TcpSocketFactory" and localAddress -> localAddress1
// 19. Replace all sinkApp -> sinkApp1 and packetSinkHelper -> packetSinkHelper1
    PacketSinkHelper packetSinkHelper1("ns3::TcpSocketFactory", localAddress1);
    ApplicationContainer sinkApp1 = packetSinkHelper1.Install(nodes.Get(2));

    sinkApp1.Start(Seconds(0.0));
    sinkApp1.Stop(Seconds(simulationTime + 0.1));
// 20. **********************************
// Comment below line
    //uint32_t payloadSize = 1448;
    Config::SetDefault("ns3::TcpSocket::SegmentSize", UintegerValue(payloadSize));
// 21. **********************************
// Replace all onoff -> onoff1 and apps -> apps1
    OnOffHelper onoff1("ns3::TcpSocketFactory", Ipv4Address::GetAny());
    onoff1.SetAttribute("OnTime", StringValue("ns3::ConstantRandomVariable[Constant=1]"));
    onoff1.SetAttribute("OffTime", StringValue("ns3::ConstantRandomVariable[Constant=0]"));
    onoff1.SetAttribute("PacketSize", UintegerValue(payloadSize));
    onoff1.SetAttribute("DataRate", StringValue("50Mbps")); // bit/s
    ApplicationContainer apps1;
// 22. **********************************
// Replace all rmt -> rmt1 and interfaces -> interfaces1
    InetSocketAddress rmt1(interfaces1.GetAddress(1), port1);
    rmt1.SetTos(0xb8);
    AddressValue remoteAddress1(rmt1);
// 23. **********************************
// Replace remoteAddress -> remoteAddress1
    onoff1.SetAttribute("Remote", remoteAddress1);
// 24. **********************************
// Replace nodes.Get(0) -> nodes.Get(3)
    apps1.Add(onoff1.Install(nodes.Get(3)));
    apps1.Start(Seconds(1.0));
    apps1.Stop(Seconds(simulationTime + 0.1));


    FlowMonitorHelper flowmon;
    Ptr<FlowMonitor> monitor = flowmon.InstallAll();

    Simulator::Stop(Seconds(simulationTime + 5));
    Simulator::Run();

    Ptr<Ipv4FlowClassifier> classifier = DynamicCast<Ipv4FlowClassifier>(flowmon.GetClassifier());
    std::map<FlowId, FlowMonitor::FlowStats> stats = monitor->GetFlowStats();
    std::cout << std::endl << "*** Flow monitor statistics ***" << std::endl;
    std::cout << "  Tx Packets/Bytes:   " << stats[1].txPackets << " / " << stats[1].txBytes
              << std::endl;
    std::cout << "  Offered Load: "
              << stats[1].txBytes * 8.0 /
                     (stats[1].timeLastTxPacket.GetSeconds() -
                      stats[1].timeFirstTxPacket.GetSeconds()) /
                     1000000
              << " Mbps" << std::endl;
    std::cout << "  Rx Packets/Bytes:   " << stats[1].rxPackets << " / " << stats[1].rxBytes
              << std::endl;
    uint32_t packetsDroppedByQueueDisc = 0;
    uint64_t bytesDroppedByQueueDisc = 0;
    if (stats[1].packetsDropped.size() > Ipv4FlowProbe::DROP_QUEUE_DISC)
    {
        packetsDroppedByQueueDisc = stats[1].packetsDropped[Ipv4FlowProbe::DROP_QUEUE_DISC];
        bytesDroppedByQueueDisc = stats[1].bytesDropped[Ipv4FlowProbe::DROP_QUEUE_DISC];
    }
    std::cout << "  Packets/Bytes Dropped by Queue Disc:   " << packetsDroppedByQueueDisc << " / "
              << bytesDroppedByQueueDisc << std::endl;

// 25. **********************************
// Comment below block              
    // uint32_t packetsDroppedByNetDevice = 0;
    // uint64_t bytesDroppedByNetDevice = 0;
    // if (stats[1].packetsDropped.size() > Ipv4FlowProbe::DROP_QUEUE)
    // {
    //     packetsDroppedByNetDevice = stats[1].packetsDropped[Ipv4FlowProbe::DROP_QUEUE];
    //     bytesDroppedByNetDevice = stats[1].bytesDropped[Ipv4FlowProbe::DROP_QUEUE];
    // }
    // std::cout << "  Packets/Bytes Dropped by NetDevice:   " << packetsDroppedByNetDevice << " / "
    //           << bytesDroppedByNetDevice << std::endl;
    // std::cout << "  Throughput: "
    //           << stats[1].rxBytes * 8.0 /
    //                  (stats[1].timeLastRxPacket.GetSeconds() -
    //                   stats[1].timeFirstRxPacket.GetSeconds()) /
    //                  1000000
    //           << " Mbps" << std::endl;
    // std::cout << "  Mean delay:   " << stats[1].delaySum.GetSeconds() / stats[1].rxPackets
    //           << std::endl;
    // std::cout << "  Mean jitter:   " << stats[1].jitterSum.GetSeconds() / (stats[1].rxPackets - 1)
    //           << std::endl;
    // auto dscpVec = classifier->GetDscpCounts(1);
    // for (auto p : dscpVec)
    // {
    //     std::cout << "  DSCP value:   0x" << std::hex << static_cast<uint32_t>(p.first) << std::dec
    //               << "  count:   " << p.second << std::endl;
    // }

    Simulator::Destroy();
// 26. **********************************
// comment this block
    // std::cout << std::endl << "*** Application statistics ***" << std::endl;
    // double thr = 0;
    // uint64_t totalPacketsThr = DynamicCast<PacketSink>(sinkApp.Get(0))->GetTotalRx();
    // thr = totalPacketsThr * 8 / (simulationTime * 1000000.0); // Mbit/s
    // std::cout << "  Rx Bytes: " << totalPacketsThr << std::endl;
    // std::cout << "  Average Goodput: " << thr << " Mbit/s" << std::endl;
    // std::cout << std::endl << "*** TC Layer statistics ***" << std::endl;
    // std::cout << q->GetStats() << std::endl;
    return 0;
}