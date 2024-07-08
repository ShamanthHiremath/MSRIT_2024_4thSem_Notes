/*
1) B.
5) B.

Design and simulate a wired network with duplex links between ‘n’ nodes with CDR over 
UDP. Set the queue size vary the bandwidth and find the number of packets dropped.
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

NS_LOG_COMPONENT_DEFINE("TrafficControlExample");

/**
 * Number of packets in TX queue trace.
 *
 * \param oldValue Old velue.
 * \param newValue New value.
 */
void
TcPacketsInQueueTrace(uint32_t oldValue, uint32_t newValue)
{
    std::cout << "TcPacketsInQueue " << oldValue << " to " << newValue << std::endl;
}

/**
 * Packets in the device queue trace.
 *
 * \param oldValue Old velue.
 * \param newValue New value.
 */
void
DevicePacketsInQueueTrace(uint32_t oldValue, uint32_t newValue)
{
    std::cout << "DevicePacketsInQueue " << oldValue << " to " << newValue << std::endl;
}

/**
 * TC Soujoun time trace.
 *
 * \param sojournTime The soujourn time.
 */
void
SojournTimeTrace(Time sojournTime)
{
    std::cout << "Sojourn time " << sojournTime.ToDouble(Time::MS) << "ms" << std::endl;
}

int
main(int argc, char* argv[])
{
    double simulationTime = 10; // seconds
    // 1.  Change Tcp -> Udp
    std::string transportProt = "Udp";
    std::string socketType;

    CommandLine cmd(__FILE__);
    cmd.AddValue("transportProt", "Transport protocol to use: Tcp, Udp", transportProt);
    cmd.Parse(argc, argv);

    if (transportProt == "Tcp")
    {
        socketType = "ns3::TcpSocketFactory";
    }
    else
    {
        socketType = "ns3::UdpSocketFactory";
    }

    NodeContainer nodes;
    // 2.   Set to number of nodes as per question
    nodes.Create(3);

    PointToPointHelper pointToPoint;
    pointToPoint.SetDeviceAttribute("DataRate", StringValue("10Mbps"));
    pointToPoint.SetChannelAttribute("Delay", StringValue("2ms"));
    pointToPoint.SetQueue("ns3::DropTailQueue", "MaxSize", StringValue("1p"));

    // 3. Make devices-> devices01
    //    Make Install(nodes) -> Install(nodes.Get(0), nodes.Get(1))
    
    NetDeviceContainer devices01;
    devices01 = pointToPoint.Install(nodes.Get(0),nodes.Get(1));

    // 4. Make devices-> devices12
    //    Make Install(nodes) -> Install(nodes.Get(0), nodes.Get(1))
    NetDeviceContainer devices12;
    devices12 = pointToPoint.Install(nodes.Get(1),nodes.Get(2));



    InternetStackHelper stack;
    stack.Install(nodes);
    // 5.  Comment the below lines

/*
    TrafficControlHelper tch;
    tch.SetRootQueueDisc("ns3::RedQueueDisc");
    QueueDiscContainer qdiscs = tch.Install(devices);

    Ptr<QueueDisc> q = qdiscs.Get(1);
    q->TraceConnectWithoutContext("PacketsInQueue", MakeCallback(&TcPacketsInQueueTrace));
    Config::ConnectWithoutContext(
        "/NodeList/1/$ns3::TrafficControlLayer/RootQueueDiscList/0/SojournTime",
        MakeCallback(&SojournTimeTrace));

    Ptr<NetDevice> nd = devices.Get(1);
    Ptr<PointToPointNetDevice> ptpnd = DynamicCast<PointToPointNetDevice>(nd);
    Ptr<Queue<Packet>> queue = ptpnd->GetQueue();
    queue->TraceConnectWithoutContext("PacketsInQueue", MakeCallback(&DevicePacketsInQueueTrace));
*/



    // 6. Make address-> address01 , interfaces -> interfaces01 , devices -> devices01
    Ipv4AddressHelper address01;
    address01.SetBase("10.1.1.0", "255.255.255.0");
    Ipv4InterfaceContainer interfaces01 = address01.Assign(devices01);

    
    // 7.  Copy above three lines and Change address,  Source IP address , devices and interfaces

    Ipv4AddressHelper address12;
    address12.SetBase("10.1.2.0", "255.255.255.0");
    Ipv4InterfaceContainer interfaces12 = address12.Assign(devices12);

    // 8.  Examples->tutorials->third.cc->line 173 (Copy below line from there)

    Ipv4GlobalRoutingHelper::PopulateRoutingTables();
    
    // Flow
    uint16_t port = 7;
    Address localAddress(InetSocketAddress(Ipv4Address::GetAny(), port));
    PacketSinkHelper packetSinkHelper(socketType, localAddress);

    //9. Make sink app 0 to 2(that is your last node)
    ApplicationContainer sinkApp = packetSinkHelper.Install(nodes.Get(2));

    sinkApp.Start(Seconds(0.0));
    sinkApp.Stop(Seconds(simulationTime + 0.1));

    uint32_t payloadSize = 1448;
    Config::SetDefault("ns3::TcpSocket::SegmentSize", UintegerValue(payloadSize));

    OnOffHelper onoff(socketType, Ipv4Address::GetAny());
    onoff.SetAttribute("OnTime", StringValue("ns3::ConstantRandomVariable[Constant=1]"));
    onoff.SetAttribute("OffTime", StringValue("ns3::ConstantRandomVariable[Constant=0]"));
    onoff.SetAttribute("PacketSize", UintegerValue(payloadSize));
    onoff.SetAttribute("DataRate", StringValue("50Mbps")); // bit/s
    ApplicationContainer apps;

// 10. Change interfaces -> interfaces12.GetAdress(1) 
    InetSocketAddress rmt(interfaces12.GetAddress(1), port);
    rmt.SetTos(0xb8);
    AddressValue remoteAddress(rmt);
    onoff.SetAttribute("Remote", remoteAddress);
// 11.  Change Get(1) -> Get(0)
    apps.Add(onoff.Install(nodes.Get(0)));
    apps.Start(Seconds(1.0));
    apps.Stop(Seconds(simulationTime + 0.1));

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
    uint32_t packetsDroppedByNetDevice = 0;
    uint64_t bytesDroppedByNetDevice = 0;
    if (stats[1].packetsDropped.size() > Ipv4FlowProbe::DROP_QUEUE)
    {
        packetsDroppedByNetDevice = stats[1].packetsDropped[Ipv4FlowProbe::DROP_QUEUE];
        bytesDroppedByNetDevice = stats[1].bytesDropped[Ipv4FlowProbe::DROP_QUEUE];
    }
    std::cout << "  Packets/Bytes Dropped by NetDevice:   " << packetsDroppedByNetDevice << " / "
              << bytesDroppedByNetDevice << std::endl;
    std::cout << "  Throughput: "
              << stats[1].rxBytes * 8.0 /
                     (stats[1].timeLastRxPacket.GetSeconds() -
                      stats[1].timeFirstRxPacket.GetSeconds()) /
                     1000000
              << " Mbps" << std::endl;
    std::cout << "  Mean delay:   " << stats[1].delaySum.GetSeconds() / stats[1].rxPackets
              << std::endl;
    std::cout << "  Mean jitter:   " << stats[1].jitterSum.GetSeconds() / (stats[1].rxPackets - 1)
              << std::endl;
    auto dscpVec = classifier->GetDscpCounts(1);
    for (auto p : dscpVec)
    {
        std::cout << "  DSCP value:   0x" << std::hex << static_cast<uint32_t>(p.first) << std::dec
                  << "  count:   " << p.second << std::endl;
    }

    Simulator::Destroy();

    std::cout << std::endl << "*** Application statistics ***" << std::endl;
    double thr = 0;
    uint64_t totalPacketsThr = DynamicCast<PacketSink>(sinkApp.Get(0))->GetTotalRx();
    thr = totalPacketsThr * 8 / (simulationTime * 1000000.0); // Mbit/s
    std::cout << "  Rx Bytes: " << totalPacketsThr << std::endl;
    std::cout << "  Average Goodput: " << thr << " Mbit/s" << std::endl;
    std::cout << std::endl << "*** TC Layer statistics ***" << std::endl;
    // 12.  Comment below line
    //std::cout << q->GetStats() << std::endl;
    return 0;
}