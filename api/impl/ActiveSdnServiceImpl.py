from api.request.base_request import post_request

auth = ('admin', 'admin')

# change the base url according to the server

# for activesdn
base_url = 'http://172.16.53.150:8181/restconf/operations/activesdn:'

# TODO for testing with mock server
# base_url = 'http://localhost:9999/'


# Future < RpcResult < InstallPathSegmentOutput >> installPathSegment(InstallPathSegmentInput
# input);
#
# Future < RpcResult < GetFlowStatisticsOutput >> getFlowStatistics(GetFlowStatisticsInput
# input);
#
# Future < RpcResult < SubscribeForLinkFloodingCheckOutput >> subscribeForLinkFloodingCheck(
#     SubscribeForLinkFloodingCheckInput
# input);

# rpc subscribe-for-link-flooding-check {
# 		input {
#     		leaf switch-id {
#     			type int32;
#     		}
#     		leaf connector-id {
#     			type int32;
#     		}
#     		leaf drop-threshold {
#     			type int32;
#     		}
#     	}
# 		output {
# 			leaf status {
# 				type string;
# 			}
# 		}
# 	}
def subscribeForLinkFloodingCheck(switch_id, connector_id, drop_threshold):
    global auth, base_url
    url = base_url + 'subscribe-for-link-flooding-check'
    data = {
        "input": {
            "switch-id": switch_id,
            "connector-id": connector_id,
            "drop-threshold": drop_threshold
        }
    }

    r = post_request(url, data, auth)

    return r


#
# Future < RpcResult < CreateSrcDstTunnelOutput >> createSrcDstTunnel(CreateSrcDstTunnelInput
# input);
#
# Future < RpcResult < LimitFlowOutput >> limitFlow(LimitFlowInput
# input);
#
# Future < RpcResult < UnsubscribeForLinkFloodingCheckOutput >> unsubscribeForLinkFloodingCheck(
#     UnsubscribeForLinkFloodingCheckInput
# input);
#
# Future < RpcResult < GetPortStatisticsOutput >> getPortStatistics(GetPortStatisticsInput
# input);
#
# Future < RpcResult < CheckElephantTcpFlowOutput >> checkElephantTcpFlow(CheckElephantTcpFlowInput
# input);
#
# Future < RpcResult < CheckNewComersOutput >> checkNewComers(CheckNewComersInput
# input);
#
# Future < RpcResult < ReRouteOutput >> reRoute(ReRouteInput
# input);
#
# Future < RpcResult < RemoveAFlowRuleFromSwitchOutput >> removeAFlowRuleFromSwitch(RemoveAFlowRuleFromSwitchInput
# input);
#
# Future < RpcResult < MigrateNetworkPathOutput >> migrateNetworkPath(MigrateNetworkPathInput
# input);
#
# Future < RpcResult < SubscribeForStatsFromSwitchOutput >> subscribeForStatsFromSwitch(SubscribeForStatsFromSwitchInput
# input);

# rpc subscribe-for-stats-from-switch {
# 		input {
# 			leaf-list switch-ids {
# 				type int32;
# 			}
# 		}
# 		output {
# 			leaf status {
# 				type string;
# 			}
# 		}
# 	}
def subscribeForStatsFromSwitch(switch_ids):
    global auth, base_url
    url = base_url + 'subscribe-for-stats-from-switch'
    data = {
        "input": {
            "switch-ids": switch_ids
        }
    }

    r = post_request(url, data, auth)

    return r


#
# Future < RpcResult < CreateSrcOnlyTunnelOutput >> createSrcOnlyTunnel(CreateSrcOnlyTunnelInput
# input);
#
# Future < RpcResult < RemoveAllFlowsFromASwitchOutput >> removeAllFlowsFromASwitch(RemoveAllFlowsFromASwitchInput
# input);
#
# Future < RpcResult < SendPacketOutOutput >> sendPacketOut(SendPacketOutInput
# input);
#
# Future < RpcResult < UnsubscribeForStatsFromSwitchOutput >> unsubscribeForStatsFromSwitch(
#     UnsubscribeForStatsFromSwitchInput
# input);
#
# Future < RpcResult < IpMutateOutput >> ipMutate(IpMutateInput
# input);
#
# Future < RpcResult < InstallFlowRuleOutput >> installFlowRule(InstallFlowRuleInput
# input);
#
# Future < RpcResult < BlockFlowOutput >> blockFlow(BlockFlowInput
# input);
#
# Future < RpcResult < SubscribeEventOutput >> subscribeEvent(SubscribeEventInput
# input);
#
# Future < RpcResult < RemoveEventFromSwitchOutput >> removeEventFromSwitch(RemoveEventFromSwitchInput
# input);
#
# Future < RpcResult < InstallNetworkPathOutput >> installNetworkPath(InstallNetworkPathInput
# input);
#
# Future < RpcResult < GetAllFlowRulesFromASwitchOutput >> getAllFlowRulesFromASwitch(GetAllFlowRulesFromASwitchInput
# input);
#
# Future < RpcResult < CreateDstOnlyTunnelOutput >> createDstOnlyTunnel(CreateDstOnlyTunnelInput
# input);
#
# Future < RpcResult < CheckUdpIcmpFlowsOutput >> checkUdpIcmpFlows(CheckUdpIcmpFlowsInput
# input);

#
# Future < RpcResult < RedirectOutput >> redirect(RedirectInput
# input);
#
# Future < RpcResult < PathMutateOutput >> pathMutate(PathMutateInput
# input);
#
# Future < RpcResult < GetAllHostsOutput >> getAllHosts();

# Future<RpcResult<FindPotentialFloodedLinkOutput>> findPotentialFloodedLink();



# rpc check-udp-icmp-flows {
# 	input {
# 		leaf switch-id {
# 			type int32;
# 		}
#
# 		leaf anomalous-rate {
# 			type int32;
# 		}
# 	}
#
# 	output {
# 		leaf-list flow-ids {
# 			type string;
# 		}
# 	}
# }

def checkUdpIcmpFlows(switch_id, anomalous_rate):
    global auth, base_url
    url = base_url + 'check-udp-icmp-flows'
    data = {
        "input": {
            "switch-id": switch_id,
            "anomalous-rate": anomalous_rate,
        }
    }

    r = post_request(url, data, auth)

    return r


# rpc check-elephant-tcp-flow {
# 	input {
# 		leaf switch-id {
# 			type int32;
# 		}
#
# 		leaf anomalous-threshold {
# 			type int32;
# 		}
# 	}
#
# 	output {
# 		leaf-list flow-ids {
# 			type string;
# 		}
# 	}
# }
def checkElephantTcpFlow(switch_id, anomalous_threshold):
    global auth, base_url
    url = base_url + 'check-elephant-tcp-flow'
    data = {
        "input": {
            "switch-id": switch_id,
            "anomalous-threshold": anomalous_threshold,
        }
    }

    r = post_request(url, data, auth)

    return r


# rpc check-new-comers {
# 		input {
# 			leaf sliding-window-size {
# 				type int32;
# 			}
#
# 			leaf new-comer-threshold {
# 				type int32;
# 			}
# 		}
#
# 		output {
# 			leaf new-comer-ratio {
# 				type int32;
# 			}
# 		}
# 	}
def checkNewComers(sliding_window_size, new_comer_threshold):
    global auth, base_url
    url = base_url + 'check-new-comers'
    data = {
        "input": {
            "sliding-window-size": sliding_window_size,
            "new-comer-threshold": new_comer_threshold,
        }
    }

    r = post_request(url, data, auth)

    return r


# rpc limit-flow {
# 		input {
# 			leaf switch-id {
# 				type int32;
# 			}
#
# 			leaf flooded-link {
# 				type int32;
# 			}
#
# 			leaf source-ip {
# 				description "Source Ip Addresses";
#                 type string {
#                     pattern
# 					'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))';
#                 }
# 			}
# 		}
#
# 		output {
# 			leaf status {
# 				type string;
# 			}
# 		}
# 	}
def limitFlow(switch_id, flooded_link, source_ip):
    global auth, base_url
    url = base_url + 'limit-flow'
    data = {
        "input": {
            "switch-id": switch_id,
            "flooded-link": flooded_link,
            "source-ip": source_ip,
        }
    }

    r = post_request(url, data, auth)

    return r


# rpc find-potential-flooded-link {
# 		input {
# 			leaf message {
# 				type string;
# 			}
# 		}
# 		output {
# 			leaf criticalLink {
# 				type string;
# 			}
# 			leaf left-switch {
#     			type int32;
#     		}
# 			leaf right-switch {
#     			type int32;
#     		}
#     		leaf left-switch-port {
#     			type int32;
#     		}
#     		leaf right-switch-port {
#     			type int32;
#     		}
# 		}
# 	}

def findPotentialFloodedLink():
    global auth, base_url
    url = base_url + 'find-potential-flooded-link'
    data = {
        "input": {
            "message": "find-potential-flooded-link"
        }
    }

    r = post_request(url, data, auth)

    return r


# rpc block-flow {
# 		input {
# 			leaf switch-id {
# 				type int32;
# 			}
#
# 			leaf flow-id {
# 				type string;
# 			}
#
# 			leaf type {
#                 type string;
# 			}
# 		}
#
# 		output {
# 			leaf status {
# 				type string;
# 			}
# 		}
# 	}
def blockFlow(switch_id, flow_id, type):
    global auth, base_url
    url = base_url + 'block-flow'
    data = {
        "input": {
            "switch-id": switch_id,
            "flow-id": flow_id,
            "type": type
        }
    }

    r = post_request(url, data, auth)

    return r


if __name__ == '__main__':
    # findPotentialFloodedLink()
    # subscribeForStatsFromSwitch([1, 9])
    # subscribeForLinkFloodingCheck(1, 4, 1)
    # checkUdpIcmpFlows(1, 20)
    # blockFlow(1, '115', 'UDP')
    # checkElephantTcpFlow(1, 4)
    blockFlow(1, '75', 'Elephant')

'''
module activesdn {
    yang-version 1;
    namespace "urn:sdnhub:tutorial:odl:activesdn";
    prefix sdn;

    import tap {prefix tap;}
    
    description "Active SDN Programming Interface";

    revision "2015-06-01" {
        description "Initial version.";
    }
    
    grouping flow-rule-specs {
    	leaf switch-id {
			mandatory true;
			description "ID of the switch generated Packet_IN";
			type int32;
		}
		leaf in-port-id {
			description "Input port of the switch that received data packet.";
    		type uint32;
        }
        leaf src-mac-address {
        	description "MAC address of the Host generated packet, e.g., 00:00:00:00:00:01";
        	type string;
        }
        leaf dst-mac-address {
        	description "MAC address of the destination Host, e.g., 00:00:00:00:00:02";
        	type string;
        }
        leaf src-ip-address {
        	description "IP address of the Host generated data packet, e.g., 10.0.0.1/32";
        	type string {
                pattern
                    '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))';
                }
        }
        leaf dst-ip-address {
        	description "IP address of the destination Host, e.g., 10.0.0.2/32";
        	type string;
        }
        leaf type-of-traffic {
            type tap:traffic-type;
        }
        leaf src-port {
        	type int32;
        }
        leaf dst-port {
        	type int32;
        }
		leaf flow-priority {
			default 10;
			type int32;
		}
		leaf idle-timeout {
			default 0;
			type int32;
		}
		leaf hard-timeout {
			default 0;
			type int32;
		}
		leaf action-output-port {
			description "Specify the ID of the output port to forward the received data packet.";
			type string;
		}
		
		leaf action-set-source-ipv4-address {
			description "This sets the IP Source value of the packet to new address, e.g., 10.0.0.1/32 -> 10.0.0.2/32.";
			type string;
		}
		
		leaf action-set-dst-ipv4-address {
			description "This sets the Destination Source value of the packet to new address, e.g., 10.0.0.1/32 -> 10.0.0.2/32.";
			type string;
		}
		
		leaf action-set-ipv4-tos {
			description "This sets the IP TOS value of the packet to change its precedence.";
			type int32;
		}
		
		leaf action-set-tcp-src-port {
			description "This sets the TCP Source Port number of the packet.";
			type int32;
		}
		
		leaf action-set-tcp-dst-port {
			description "This sets the TCP Destination Port number of the packet.";
			type int32;
		}
		
		leaf action-set-ipv4-ttl {
			description "This sets the TTL value of the packet.";
			type uint8;
		}
		leaf action-set-port-queue {
			description "Set the queue on the output port";
			type int32;
		}
    }
    
    rpc install-flow-rule {
    	input {
    		uses flow-rule-specs;
    	}
    	output {
    		leaf flow-id {
    			type string;
    		}
    		leaf status {
    			type string;
    		}
    	}    
    }
	
    rpc get-all-flow-rules-from-a-switch{
    	input {
    		leaf switch-id {
    			type int32;
    		}
    	}
    	output {
    		list flow-rules {
    			key "flow-id";
    			leaf flow-id {
    				type string;
    			}
    			uses flow-rule-specs;
    		}
    	}
    }
    
    rpc remove-event-from-switch {
    	input {
    		leaf switch-id {
                type int32;
            }
    		leaf event-id {
    			type string;
    		}
    	}
    	output{
    		leaf status{
    			type string;
    		}
    	}
    }
    
    /////////////////////////////////////////////////////////////////////////////
	////--------------------Create Event RPC--------------------------------//// 
	/////////////////////////////////////////////////////////////////////////////
    grouping event-specs {
    	leaf switch-id {
			mandatory true;
			description "ID of the switch generated Packet_IN";
			type int32;
		}
		leaf in-port-id {
			description "Input port of the switch that received data packet.";
    		type uint32;
        }
        
		leaf src-mac-address {
        	description "MAC address of the Host generated packet, e.g., 00:00:00:00:00:01";
        	type string;
        }
        leaf dst-mac-address {
        	description "MAC address of the destination Host, e.g., 00:00:00:00:00:02";
        	type string;
        }
        leaf src-ip-address {
        	description "IP address of the Host generated data packet, e.g., 10.0.0.1/32";
        	type string;
        }
        leaf dst-ip-address {
        	description "IP address of the destination Host, e.g., 10.0.0.2/32";
        	type string;
        }
        
        leaf traffic-protocol {
            type tap:traffic-type;
        }
		leaf count{
        	type uint32;
        }
        leaf duration {
        	type uint32;
        }
        leaf hold-notification {
        	description "This value is used only for Drop & Notify case where if you want to hold notification immediately after drop.";
        	type int32;
        }
		leaf event-action{
			type enumeration {
	            enum DROP;
	            enum NOTIFY;
	            enum DROPANDNOTIFY;
	        }
		}
    }
    rpc subscribe-event{
    	input {
    		uses event-specs;
    	}
    	output{
    		leaf status{
    			type string;
    		}
    		leaf event-id {
    			type string;
    		}
    	}
    }
	/////////////////////////////////////////////////////////////////////////////
	////--------------------Network Management Related RPCs-----------------//// 
	/////////////////////////////////////////////////////////////////////////////
    rpc remove-all-flows-from-a-switch {
		input {
			leaf switch-id {
	            mandatory true;
	            type int32;
	        }
		}
		output {
			leaf status {
				type string;
			}
		}
	}
    
    rpc get-all-hosts {
		output {
    		list hosts-info {
                key "id";
                leaf id {
                	type uint32;
                }
                uses tap:host-info;
            }
    	}
	}
    
    rpc remove-a-flow-rule-from-switch {
		input {
			leaf switch-id {
				type int32;
			}
			leaf flow-key {
				type string;
			}
		}
		output {
			leaf status {
				type string;
			}
		}
	}
    
    rpc send-packet-out {
    	input {
    		leaf switch-id {
    			type int32;
    		}
    		leaf payload {
    			type binary;
    		}
    		leaf in-port-number {
    			type int32;
    		}
    		leaf output-port {
    			type string;
    		}
    	}
    	output {
    		leaf status {
    			type string;
    		}
    	}
    }
    /////////////////////////////////////////////////////////////////////////////
	////--------------------Install & Migrate NetworkPathRPC-----------------//// 
	/////////////////////////////////////////////////////////////////////////////
    rpc install-network-path {
		input {
			leaf src-ip-address {
                type string;
            }
			leaf dst-ip-address {
                type string;
            }
			leaf-list switches-in-path {
				min-elements 1;
				type int32;
			}
			leaf type-of-traffic {
	            type tap:traffic-type;
	        }
			leaf flow-priority {
				default 200;
				type int32;
			}
			leaf idle-timeout {
				default 0;
				type int32;
			}
			leaf hard-timeout {
				default 0;
				type int32;
			}
		}
		output {
			leaf status {
				type string;
			}
		}
	}
    
    rpc re-route {
		input {
			leaf src-ip-address {
                type string;
            }
			leaf dst-ip-address {
                type string;
            }
			leaf-list switches-in-old-path {
				min-elements 1;
				ordered-by user;
				type int32;
			}
			leaf-list switches-in-new-path {
				min-elements 1;
				ordered-by user;
				type int32;
			}
			leaf remove-old-path {
				type boolean;
			}
			leaf flow-priority {
				default 200;
				type int32;
			}
			leaf idle-timeout {
				default 0;
				type int32;
			}
			leaf hard-timeout {
				default 0;
				type int32;
			}
		}
		output {
			leaf status {
				type string;
			}
		}
	}
    
    rpc migrate-network-path {
		input {
			leaf old-src-ip-address {
				description "It is assumed that this filed must be provided";
                type string;
            }
			leaf new-src-ip-address {
				description "This field may left empty";
                type string;
            }
			leaf old-dst-ip-address {
                type string;
            }
			leaf new-dst-ip-address {
                type string;
            }
			leaf-list switches-in-old-path {
				min-elements 1;
				type int32;
			}
			leaf-list switches-in-new-path {
				min-elements 1;
				type int32;
			}
			leaf flow-priority {
				default 200;
				type int32;
			}
			leaf idle-timeout {
				default 0;
				type int32;
			}
			leaf hard-timeout {
				default 0;
				type int32;
			}
		}
		output {
			leaf status {
				type string;
			}
		}
	}
	
    rpc redirect {
    	input {
			leaf src-ip-address {
                type string;
            }
			leaf dst-ip-address {
                type string;
            }
			leaf-list switches-in-path {
				min-elements 1;
				type int32;
			}
			leaf inspection-switch-id {
				type int32;
			}
			leaf inspection-switch-port-id {
				type string;
			}
			leaf type-of-traffic {
	            type tap:traffic-type;
	        }
			leaf flow-priority {
				default 200;
				type int32;
			}
			leaf idle-timeout {
				default 0;
				type int32;
			}
			leaf hard-timeout {
				default 0;
				type int32;
			}
		}
		output {
			leaf status {
				type string;
			}
		}
    }
    
    rpc install-path-segment {
		input {
			leaf src-ip-address {
                type string;
            }
			leaf dst-ip-address {
                type string;
            }
			leaf-list switches-in-path {
				min-elements 1;
				type int32;
			}
			leaf flow-priority {
				type int32;
			}
			leaf idle-timeout {
				type int32;
			}
			leaf hard-timeout {
				type int32;
			}
		}
		output {
			leaf status {
				type string;
			}
		}
	}
    /////////////////////////////////////////////////////////////////////////////
	////--------------------Create End-to-End-Tunnels -----------------------//// 
	/////////////////////////////////////////////////////////////////////////////
    rpc get-flow-statistics {
    	input {
    		leaf switch-id {
    			type int32;
    		}
    	}
    	output {
    		leaf switch-id {
    			type int32;
    		}
    		uses grp-flow-statistic;
    		
    		leaf status {
    			type string;
    		}
    	}
    }
    
    rpc get-port-statistics {
    	input {
    		leaf switch-id {
    			type int32;
    		}
    		leaf connector-id {
    			type int32;
    		}
    	}
    	output {
    		uses grp-port-statistics;
    	}
    }
    
    grouping grp-port-statistics {
    	leaf total-transmitted {
			type uint32;
		}
    	leaf total-received {
    		type uint32;
    	}
		leaf receive-drops {
			type uint32;
		}
		leaf transmit-drops {
			type uint32;
		}
    }
    
	grouping grp-flow-statistic {
		list flow-statistic {
			key "flow-id";
			leaf flow-id {
				type string;
			}
			leaf packet-count {
				type uint64;
			}
			leaf byte-count {
				type uint64;
			}
			leaf duration {
				type uint32;
				description "time window in seconds";
				default 0;
			}
			leaf src-ip-address {
	        	description "IP address of the Host generated data packet, e.g., 10.0.0.1/32";
	        	type string;
	        }
	        leaf dst-ip-address {
	        	description "IP address of the destination Host, e.g., 10.0.0.2/32";
	        	type string;
	        }
	        leaf type-of-traffic {
	            type tap:traffic-type;
	        }
	        leaf src-port {
	        	type int32;
	        }
	        leaf dst-port {
	        	type int32;
	        }
		}
    }
	
	rpc subscribe-for-stats-from-switch {
		input {
			leaf-list switch-ids {
				type int32;
			}
		}
		output {
			leaf status {
				type string;
			}
		}
	}
	
	rpc unsubscribe-for-stats-from-switch{
		input {
			leaf switch-id {
				type int32;
			}
		}
		output {
			leaf status {
				type string;
			}
		}

	}
	
	
	
	rpc unsubscribe-for-link-flooding-check {
		input {
    		leaf switch-id {
    			type int32;
    		}
    		leaf connector-id {
    			type int32;
    		}
    	}
		output {
			leaf status {
				type string;
			}
		}
	}
	
    /////////////////////////////////////////////////////////////////////////////
	////--------------------Create End-to-End-Tunnels -----------------------//// 
	/////////////////////////////////////////////////////////////////////////////
    rpc create-src-only-tunnel {
		input {
			leaf current-src-ip-address {
                type string;
            }
			leaf new-src-ip-address {
                type string;
            }
			leaf dst-ip-address {
                type string;
            }
			leaf-list switches-in-path {
				min-elements 1;
				type int32;
			}
			leaf flow-priority {
				default 200;
				type int32;
			}
			leaf idle-timeout {
				default 0;
				type int32;
			}
			leaf hard-timeout {
				default 0;
				type int32;
			}
		}
		output {
			leaf status {
				type string;
			}
		}
	}
    
    rpc create-dst-only-tunnel {
		input {
			leaf src-ip-address {
                type string;
            }
			leaf current-dst-ip-address {
                type string;
            }
			leaf new-dst-ip-address {
                type string;
            }
			leaf-list switches-in-path {
				min-elements 1;
				type int32;
			}
			leaf flow-priority {
				default 200;
				type int32;
			}
			leaf idle-timeout {
				default 0;
				type int32;
			}
			leaf hard-timeout {
				default 0;
				type int32;
			}
		}
		output {
			leaf status {
				type string;
			}
		}
	}
    
    rpc create-src-dst-tunnel {
		input {
			leaf current-src-ip-address {
                type string;
            }
			leaf new-src-ip-address {
                type string;
            }
			leaf current-dst-ip-address {
                type string;
            }
			leaf new-dst-ip-address {
                type string;
            }
			leaf-list switches-in-path {
				min-elements 1;
				type int32;
			}
			leaf flow-priority {
				default 200;
				type int32;
			}
			leaf idle-timeout {
				default 0;
				type int32;
			}
			leaf hard-timeout {
				default 0;
				type int32;
			}
		}
		output {
			leaf status {
				type string;
			}
		}
	}
    
    rpc ip-mutate {
		input {
			leaf old-src-ip-address {
				type string;
            }
			leaf new-src-ip-address {
				type string;
            }
			leaf old-dst-ip-address {
				type string;
            }
			leaf new-dst-ip-address {
				type string;
            }
			leaf-list switches-in-path {
				min-elements 1;
				type int32;
			}
			leaf flow-priority {
				default 200;
				type int32;
			}
			leaf idle-timeout {
				default 0;
				type int32;
			}
			leaf hard-timeout {
				default 0;
				type int32;
			}
		}
		output {
			leaf status {
				type string;
			}
		}
	}
    
    
    /////////////////////////////////////////////////////////////////////////////
    ////--------------------IP Packet Header Fields--------------------------//// 
    /////////////////////////////////////////////////////////////////////////////
    grouping ipv4-packet-header-fields {
        leaf version {
          type uint8;
        }

        leaf ihl {
          type uint8;
          description "Internal Header Length";
        }

        leaf dscp-value {
          type uint8;
          description "Differentiated Code Services Point";
        }

        leaf ecn {
          type uint8;
          description "Explicit Congestion Notification";
        }

        leaf total-length {
          type uint16;
          description "Packet size, including header and data, in bytes";
        }

        leaf identification {
          type uint16;
          description "Identification";
        }

        leaf reserved-flag {
          type boolean;
          description "First bit in the flags, must be 0";
        }

        leaf df-flag {
          type boolean;
          description "Second bit in the flags, Don't Fragment Flag";
        }

        leaf mf-flag {
          type boolean;
          description "Third bit in the flags, More Fragments Flag";
        }

        leaf fragment-offset {
          type uint16;
          description "Specifies the offset of a particular fragment relative to the beginning of the original unfragmented IP datagram";
        }

        leaf ttl {
          type uint8;
          description "Time to live";
        }

        leaf protocol {
          type uint8;
          description "Protocol for the data";
        }

        leaf header-checksum {
          type uint16;
          description "Header Checksum";
        }

        leaf source-address {
          type string;
        }

        leaf destination-address {
          type string;
        }
        leaf ipv4-options {
            type binary; 
        }  
    }

    grouping arp-packet-header-fields {
         leaf ethernet-src-mac-address {
        	 type string;
         }
         leaf ethernet-type {
        	 type string;
         }
         leaf hardware-type {
        	 type string;
         }
         leaf protocol-type {
        	 type string;
         }
         leaf hardware-address-length {
        	 type int32;
         }
         leaf protocol-address-length {
        	 type int32;
         }
         leaf opcode {
        	 type string;
         }
         leaf sender-hardware-address {
        	 type string;
         }
         leaf sender-protocol-address {
        	 type string;
         }
         leaf target-hardware-address {
        	 type string;
         }
         leaf target-protocol-address {
        	 type string;
         }
    }
   
    grouping icmp-packet-header-fields {
    	leaf ethernet-src-mac-address {
       	 type string;
        }
        leaf ethernet-type {
       	 type string;
        }
        leaf type {
        	type uint8;
        }
        leaf code {
        	type uint8;
        }
        leaf crc {
            type uint16;
        }

        leaf identifier {
            type uint16;
        }

        leaf sequence-number {
            type uint16;
        }
    }
    
    grouping tcp-packet-header-fields {
        leaf source-port {
          type int16;
        }

        leaf dest-port {
            type int16;
        }

        leaf sequence-number {
            type int32;
        }
        
        leaf syn-flag {
            type boolean;
        }
        
        leaf rst-flag {
            type boolean;
        }
        
        leaf ack-flag {
            type boolean;
        }
        
        leaf fin-flag {
            type boolean;
        }
    }
    /////////////////////////////////////////////////////////////////////////////
    ////--------------------Notifications Generated detail-------------------//// 
    /////////////////////////////////////////////////////////////////////////////
    notification event-triggered {
    	leaf triggered-event-type {
    		type enumeration {
    			enum NoFlowRuleEvent;
    			enum ControllerFlowRuleEvent;
    			enum SubscribedEvent;
    		}
    	}
    	leaf event-id {
    		type string;
    	}
    	leaf switch-id {
    		type int32;
    	}
    	leaf in-port-number {
    		type int32;
    	}
    	choice packet-type {
    		case ipv4-packet-type {
    			uses ipv4-packet-header-fields;
    		}
    		case arp-packet-type {
    			uses arp-packet-header-fields;
    		}
    		case icmp-packet-type {
    			uses icmp-packet-header-fields;
    			 uses ipv4-packet-header-fields;
    			 leaf icmp-payload-offset {
   	    	      type int32;
   	    	    }
   	    	    leaf icmp-payload-length {
   	    	      type int32;
   	    	    }
    		}
    		case tcp-packet-type {
    			uses ipv4-packet-header-fields;
    			uses tcp-packet-header-fields;
    		}
    	}
    	leaf payload {
     	      type binary;    
    	}
    	leaf string-payload {
    		type string;
    	}
    }

    notification new-host-found {
    	leaf host-mac-address {
			type string;
		}
		leaf host-ip-address {
			type string;
		}
		leaf switch-connected-to {
			type int32;
		}
		leaf port-connected-to {
			type int32;
		}
    }

    notification construct-topology {
    	
    }
    
    notification flow-is-removed {
    	leaf switch-id {
    		type int32;
    	}
    	leaf flow-id {
    		type string;
    	}
    }
    
    notification flow-statistic-received {
    	list switch-statistics {
    		key "switch-id";
    		leaf switch-id {
    			type int32;
    		}
    		uses grp-flow-statistic;
    	}
    	leaf stats-time {
			type uint32;
		}
    }
    
    notification is-link-flooded {
    	list flooded-links {
    		key "link-id";
    		leaf link-id {
    			type string;
    		}
    		leaf packet-drop-observed {
    			type uint32;
    		}
    	}
    }
    
//    notification is-dropbox-detected {
//    	container dropbox-info {
//    		leaf srcIp{
//    			type string;
//    		}
//    		leaf dstPort {
//    			type int32;
//    		}
//    		leaf dstIp {
//    			type string;
//    		}
//    	}
//    }
    //////////////////////////////////////////////////////////////////////////////////
    ////////---------------------RPCs created by Rakeb-------------------------------///////////
    /////////////////////////////////////////////////////////////////////////////////
	rpc path-mutate {
        input {
            leaf-list src {
                description "List of source Ip Addresses";
                min-elements 1;
                ordered-by user;
                type string {
                    pattern
                                        '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))';
                }
            }
            leaf-list dst {
                description "List of destination Ip Addresses";
                min-elements 1;
                ordered-by user;
                type string {
                    pattern
                                        '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))';
                }
            }
            leaf overlap {
                type string;
            }
            leaf max-path-length {
                type string;
            }
            leaf available-bandwidth {
                type string;
            }
            leaf pattern {
                type int32;
            }
        }
        output {
            leaf status {
                type string;
            }
        }
    }
	
	rpc check-udp-icmp-flows {
		input {
			leaf switch-id {
				type int32;
			}
			
			leaf anomalous-rate {
				type int32;
			}
		}
		
		output {
			leaf-list flow-ids {
				type string;
			}
		}
	}
	
	rpc check-elephant-tcp-flow {
		input {
			leaf switch-id {
				type int32;
			}
			
			leaf anomalous-threshold {
				type int32;
			}
		}
		
		output {
			leaf-list flow-ids {
				type string;
			}
		}
	}
	
	rpc check-new-comers {
		input {
			leaf sliding-window-size {
				type int32;
			}
			
			leaf new-comer-threshold {
				type int32;
			}
		}
		
		output {
			leaf new-comer-ratio {
//				type decimal64 {
//					fraction-digits 2;
//				}
				type int32;
			}
		}
	}
	
	rpc limit-flow {
		input {
			leaf switch-id {
				type int32;
			}
			
			leaf flooded-link {
				type int32;
			}
			
			leaf source-ip {
				description "Source Ip Addresses";
                type string {
                    pattern
					'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))';
                }
			}
		}
		
		output {
			leaf status {
				type string;
			}
		}
	}
	
	rpc block-flow {
		input {
			leaf switch-id {
				type int32;
			}
			
			leaf flow-id {
				type string;
			}
			
			leaf type {
                type string;
			}
		}
		
		output {
			leaf status {
				type string;
			}
		}
	}
	
	rpc find-potential-flooded-link {
		input {
			leaf message {
				type string;
			}
		}
		output {
			leaf criticalLink {
				type string;
			}
			leaf left-switch {
    			type int32;
    		}
			leaf right-switch {
    			type int32;
    		}
    		leaf left-switch-port {
    			type int32;
    		}
    		leaf right-switch-port {
    			type int32;
    		}
		}
	}

	  
    
    /*
    rpc canReach{
    	input {
    		leaf src-ip-address {
            	description "IP address of the Host generated data packet, e.g., 10.0.0.1/32";
            	type string {
                    pattern
                        '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))';
                    }
            }
    		leaf dst-ip-address {
            	description "IP address of the Host generated data packet, e.g., 10.0.0.1/32";
            	type string {
                    pattern
                        '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))';
                    }
            }
    	}
    	output {
    		leaf status {
    			type boolean;
    		}
    	}
    }
    */
}

'''
