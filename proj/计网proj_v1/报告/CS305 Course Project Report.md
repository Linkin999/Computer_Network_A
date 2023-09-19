<h1 align = "center"><font size='6'>CS305 Course Project: Research on IPv6 Network Protocol</h1>

<h1 align = "center"><font size='4'>Name: 吉辰卿（狗男人） &nbsp&nbsp张旭东 &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp ID: 11911303&nbsp &nbsp 12011923</h1>



## Part 1: Basic information about IPv6

### 1.1 Motivation of development of IPv6

​	As new subnets and IP nodes connect to the Internet at an alarming rate and are assigned unique IP addresses, the address  space represented by 32 bits is running out. To satisfy the requirement for a larger IP addresses space, a new IP protocol was developed, which was named IPv6. This was also an opportunity to improve and strengthen other aspects of IPv4 based on the operational experience accumulated in IPv4.

​	Additional motivation is that header format helps speed processing and forwarding and facilitate quality of service.

### 1.2 Characteristics of IPv6

#### 1.2.1 Larger address space

​	Different from IPv4, whose length of an IP address is only 32 bits, IPv6 increases the length of an IP address from 32 bits to 128 bits, which makes sure the world doesn't run out of IP addresses. What's more, IPv6 has introduced a new type of address called the anycast address,which can deliver datagrams to any one of a set of hosts.

#### 1.2.2 Simplified and efficient packet structure

​	The header length of IPv4 is not fixed, which is caused by the $option$ header field whose length is indefinite. The header length of IPv6 is fixed, which is 40 bytes. The 40-byte fixed-length header allows the routers to process IP packets faster, which can improve the quality of service.

#### 1.2.3 Better scalability

​		As discussed above, IPv6 fixes the header length and transfers the functionality of the option field and fragment field to its extended header, which allows more flexible processing of options to do. More functionality can be achieved by adding different extended headers.

#### 1.2.4 Flow label

​	The IPv6 packet format has a flow label field whose length is 20 bits. It is used to identify the flow of a packet and can give priority to some datagrams in a flow, or it can be used to give higher priority to some applications' datagrams over those from other applications.

#### 1.2.5 Implementation of automatic configuration and prefix re - addressing

​	On an IPv6 network, a router advertises its interface prefix to end system. End system generates an available IPv6 address for itself by using this prefix and calculating the generated interface ID, and also considers the route as its default gateway. Even if the end system that has obtained an IPv6 address is moved to another network segment, the end system can automatically change its IPv6 address through the above process.

#### 1.2.6 Support for hierarchical network structure

​		IPv6 addresses are assigned in order from IANA to RIR and then to ISP. IANA is the International Assigned Numbers Authority,  RIR is the Regional Internet Registry, and ISP is Internet Service Provider. IANA will reasonably assign IPv6 addresses to the five RIRs. Then, the RIR allocates addresses to the countries in the region reasonably. The addresses assigned to each country are then handed over to ISPs. Last, ISPs allocate IPv6 addresses to users reasonably. 

​	In this assignment process, the case that the network addresses of subnets are discontinuous can be avoided as much as possible, which can better aggregate routes and reduce the number of route entries on the backbone network.

#### 1.2.7 Better support for quality of service

​	IPv6 protocol supports quality of service better in two aspects. One is that  the priority field of IPv6 protocol has 6 bits that can be used as a priority representation and can represent 64 different priorities. The other is that the flow label field in IPv6 protocol defines a data flow based on the source and destination addresses.

​	In the early stage, a flow classifier defines a data flow only through the quintuple of source IP address, destination IP address, source port, destination port, and protocol. This definition process can be defined only after being unpackaged at the transport layer. With the flow label field, flow classification can be realized directly through the information of the network layer, which greatly improves the efficiency of flow classification.

#### 1.2.8 Native support for end-to-end security

​	The extended header of IPv6 protocol includes an authentication header and an encapsulation security clean-load header, which are defined by IPsec protocol. The network layer can implement end-to-end security through these two headers without assistances from other protocols, as is the case for IPv4 protocol.

#### 1.2.9 Support for mobile features

​	IPv6 protocol supports the mobile of end system. It means that communication can also be quickly recovered when the end system is moved to another network environment. However,it's just a concept, not in use yet.

#### 1.2.10 Other differences between IPv4 and IPv6

- ​	Fragmentation and Reassembly

  IPv4 protocol allows fragmentation in the router. However, IPv6 protocol doesn't allow this operation happened in the router. For IPv6 protocol, fragmentation is allowed only at source and destination. If the size of received IPv6 datagrams is too large, the router discards the datagram and sends back an ICMP error datagram.  Fragmentation and reassembly is a time-consuming operation, and removing this function from the router and placing it on the end system greatly speeds up IP datagram forwarding through the network.

-    Checksum in the header

  For IPv4 protocol, checksum in the header needs to be recalculated on each router. However, this will never happen for IPv6 protocol. Removing this operation will speed up the processing of IP packets.

- Option

  For IPv4 protocol, the option field is a part of the standard IP header. However, for IPv6 protocol, it is no longer a part of standard IP header. It may appear  at the location indicated by the "next header" field in the IPv6 datagram.

### 1.3 Development of IPv6

#### 1.3.1 Status of development of IPv6

- Countries actively reserve IPv6 address resources

  More than 220 countries and regional organizations in the world have applied for IPv6 addresses, which has reached more than 180,000 times of the current Internet address space, and 25.4% of the address blocks have been notified for use.

- Steady progress in building network infrastructure

  Among the 13 root DNS servers in the world, 11 of them support IPv6 protocol. Among the 1346 top-level DNS servers, 1318 of them support IPv6 protocol, which accounts for 97.9 percent of the total . The upgrade of DNS servers has laid a solid foundation for the full commercial deployment of IPv6 protocol.

- Rapidly growing commercial network scale

  At present, there are more than 29,000 active route entries of IPv6 protocol in the world, more than 11,800 autonomous regions that support IPv6 protocol, and more than 248 ISPs providing permanent access services to IPv6 protocol, basically forming an network of IPv6 protocol covering major ISPs, content service providers and economic regions.

- The content that can be accessed by IPv6 protocol becomes more and more abundant

  More than 195 million website domain names have been registered worldwide, of which 7.63 million domain names support the type  "AAAA " of record of IPv6 protocol, accounting for 3.90% of the total. Meanwhile, a growing number of mobile apps are also providing support for IPv6 protocol.

- Growing user scale

  At present, more than 94 countries have developed users of IPv6 protocol, and the total number of users is more than 250 million.

- Mobile traffic is the main growth point

  The growth of users, the expansion of network coverage and the richness of content have contributed to the significant growth of global data traffic of TPv6 protocol. The average traffic of IPv4 protocol reached 45.4 gigabytes, accounting for more than 34% of the global traffic.

- Mobile end operating systems have further improved their support for IPv6

  The latest Android and Windows Phone systems include a component  named 464xlatCLAT, which encapsulates packets of IPv4 through an tunnel of IPv6 and sends them to the gateway named NAT64 to access sources of IPv4.

#### 1.3.2 Resistance to the development of IPv6 

1. The exhaustion process of IPv4 addresses slows down

   The widespread use of classless interdomain routing and NAT has slowed the process of exhaustion of IPv4 addresses. What's more, it is difficult for the smooth evolution of the technology due to the incompatibility of IPv6 protocol and IPv4 protocol. 

2. The lack of a reasonable business model

   In the short term, it is difficult for deployers to gain benefits from technology upgrade. Moreover, technology upgrade is a complex system engineering, which requires multiple links from end to end and training of relevant technical persons.

3. The disadvantages of IPv6 protocol

   - Low efficiency
   - Security algorithms are controlled in the United States
   -  The digital button can't be used to access the Internet
   - The IP addresses can't be directly represented and must be translated by DNS
   - The algorithm used to connect the network is complex
   - There is no fundamental solution to the image and sound protocol

#### 1.3.3 Status of migration from IPv4 to IPv6

​	There are three main ways to migrate from IPv4 to IPv6, which are double stack technique, tunneling technique and protocol translation technique.

- double stack technique

  <img src="D:\Study in SUSTech\First semester of junior year\Computer Network A\proj\计网proj_v1\报告\double stack.png" style="zoom:50%;" />

  IPv6 protocol and IPv4  protocol are network layer protocols with similar functions. Both are based on the same physical platform, and there is no difference between the transport layer protocols loaded on them, which are TCP and UDP. Therefore, a host that supports both IPv6 protocol and IPv4 protocol can communicate with hosts that support IPv4 protocol and hosts that support IPv6 protocol.

- tunneling technique

  <img src="D:\Study in SUSTech\First semester of junior year\Computer Network A\proj\计网proj_v1\报告\tunneling.png" style="zoom:50%;" />

  When an IPv6 datagram enters an IPv4 network, the IPv6 datagram is encapsulated into an IPv4 datagram. When the encapsulated IPv4 datagram leaves the IPv4 network, the data portion (IPv6 datagram) is taken out and forwarded to the destination node. The router encapsulates the IPv6 datagram into an IPv4 datagram. The source and destination addresses of the IPv4 datagram are the IPv6 addresses of the tunnel entrance and exit, respectively.

  The tunnel technique can connect the local IPv6 network through the existing Internet backbone network running IPv4 protocol, so it is the easiest technology to adopt in the early stage of the transition from IPv4 to IPv6.

- protocol translation technique

  By combining SIIT protocol translation with traditional IPv4 dynamic address translation and appropriate application layer gateway , it enables the communication for most applications between hosts that only support IPv6 and hosts that only support IPv4. 

#### 1.3.4 Difficulties in the migration process from IPv4 to IPv6

- double stack technique

  This technique has high requirements for sites,and may involve upgrade of servers and network equipment. It is a long-term evolution technology with large investment and long transformation period. In the short term, it is suitable for the upgrade of websites of IPv6 with relatively simple architecture and services. Because the codes of IPv4 and IPv6 are not exactly the same, the codes of double stacks of website applications need to be rewritten. 

- tunneling technique

  This technology requires users to install corresponding tunnel software of IPv6, which has limitations in universality and convenience. It is mainly applicable to the application environment of the C/S model or the scenario where users can install end system, but is not suitable for large-scale deployment.

### 1.4 Outside attitudes towards IPv6

- Strong support from domestic policies

  In November 2017, the General Office of the CPC Central Committee and The General Office of the State Council jointly issued the Action Plan for Promoting the Large-scale Deployment of Internet Protocol Version 6. The Action Plan calls for the formation of an independent technology system and industrial ecosystem of the next generation of Internet, the world's largest IPv6 commercial application network, and the deep integration of the next generation of Internet in various economic and social fields in 5 to 10 years.

  In October 2018, the Yunnan Provincial government issued the Implementation Opinions on Promoting the Deployment Plan of IPv6 . Through government guidance and enterprise leadership, by the end of 2020, the active users of IPv6 will exceed 20 million, accounting for more than 50% of the Internet users. By the end of 2025, networks, applications, and end system will fully support IPv6.

- Strong promotion from international policy

  1. IPv6 in American

     The US government is one of the most important users of the applications of IPv6 in the US. It has publicly declared many times that IPv6 plays a key role in the sustainable development of the Internet economy in the US, and has forced the implementation of upgrade of IPv6. The U.S. government has already issued a deadline for the military to transition to IPv6, as well as a deadline for all levels of the federal government to fully complete the support of IPv6.

  2. IPv6 in Europe

     The governments of European countries have adopted a unified policy to provide tax breaks and market information support for products that support IPv6. Europe's Third Generation Partnership has defined IPv6 as the standard addressing scheme for mobile multimedia

  3. IPv6 in other country

     The Japanese government attaches great importance to the development of IPv6, and even regards the development of IPv6 technology as a basic policy of the government's "ultra-high speed network construction and competition". In March 2001, the "E-Japan Key Plan" put forward the goal of completing the transition of the Internet to IPv6.

- Strong push from various industries

  

  

### 1.5 Application of IPv6

​	IPv6 is widely used in various fields and scenarios.

- Applications in websites and apps

  1. In the past, the server could only see the user's home gateway or 4G gateway, which lost a lot of big data. However, using IPv6 allows servers to bypass NAT and see the end user directly, which enables accurate analysis and service.

  2. The live broadcast using IPv6 eliminates the NAT process and smoother P2P sharing technique, making the user's viewing experience more smooth. Meanwhile, accurate address positioning is not only conducive to more effective traffic guidance, but also conducive to the precise delivery of personalized advertisements, and improve the security of copyright procurement and copyright protection.

     <img src="D:\Study in SUSTech\First semester of junior year\Computer Network A\proj\计网proj_v1\报告\application in websites and apps.png" style="zoom:50%;" />

- Applications in end-to-end communication

  1. It can optimize the export of education network, ensure that the special channel of high-quality education resources is smooth, resources are delivered nearby, and improve the visiting experience of teachers and students. It can also effectively screen and classify high-quality educational resources and eliminate bad applications.

     <img src="D:\Study in SUSTech\First semester of junior year\Computer Network A\proj\计网proj_v1\报告\application in end-end communication.png" style="zoom:50%;" />

  2. At present, due to the lack of fixed IP for home cameras, people usually need to use the cloud platform to penetrate the Intranet and realize the access to the camera from the outside network, which increases the risk of the disclosure of user privacy. IPv6 provides a separate fixed IP address for home cameras, which simplifies the network structure. People can access the camera directly from their phones, reducing the risk of third-party intervention.

     <img src="D:\Study in SUSTech\First semester of junior year\Computer Network A\proj\计网proj_v1\报告\appication in home camera.png" style="zoom:50%;" />

- Applications in the field of IoT

  IPv6 integrates cutting-edge technologies such as artificial intelligence, big data and the Internet of Things, giving birth to new business forms, applications and scenarios such as smart city, smart transportation and ubiquitous electric Internet of Things.

  1. Smart transportation

     Due to the massive IPv6 address resources, the smart lock of shared bikes does not need to be connected for a long time. This saves power for the smart lock and helps reduce maintenance costs.

     <img src="D:\Study in SUSTech\First semester of junior year\Computer Network A\proj\计网proj_v1\报告\application in smart transportion.png" style="zoom:50%;" />

  2. Smart lighting

     Smart lighting based on IPv6 realizes the monitor of lighting status, which can monitor the running status of all kinds of equipment and discover the faulty equipment in time. It also realizes the analysis of operation status and energy consumption to achieve the optimization of intelligent evaluation and control of lighting effect.

     <img src="D:\Study in SUSTech\First semester of junior year\Computer Network A\proj\计网proj_v1\报告\application in smart lighting.png" style="zoom:50%;" />

  3. ubiquitous electric IoT

     Currently, more than 500 million end devices are connected to the national grid system. By 2030, it is expected to exceed 2 billion. IPv6 provides massive address resources to connect all end devices.

     <img src="D:\Study in SUSTech\First semester of junior year\Computer Network A\proj\计网proj_v1\报告\appication in electric IoT .png" style="zoom:50%;" />

## Part2:Advanced topic of IPv6
