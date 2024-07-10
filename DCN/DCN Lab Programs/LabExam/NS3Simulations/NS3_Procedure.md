## Steps

1. Go to Downloads folder and open ns-allinone-3.39/ns-3.39 folder.
2. In Example folder go to traffic-control folder and copy traffic-control.cc file.
3. Paste the file in ns-3.39/scratch folder.
4. Rename traffic-control.cc to your desired name.
5. There should be only one .cc file in the scratch folder.
6. Do necessary changes in the scratch folder.
7. Open terminal in ns-3.39 folder and run the following command:
   ```
   ./ns3 run filename --vis
   ```
8. Simulate the network (Simulation button) then you'll get Flow Monitor Statistics.

## Note:
Sink Node: End Node
Interface Node: Middle Node
App Node: Start Node