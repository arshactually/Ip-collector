from pythonping import ping
print("--IP Differentiator:--\n")
num = int(input("What range do you want to set?: "))

# List of IP addresses to ping
ip_addresses = [f"192.168.1.{i}" for i in range(1,num)]

# Dictionary mapping IP addresses to PC names
ip_to_pc = {
    "192.168.1.1": "NetGear",
    "192.168.1.3": "Martin's PC",
    "192.168.1.4": "My PC",
    "192.168.1.5": "HCC BANANA"
   
}
for ip in ip_addresses:
    if ip in ip_to_pc:
        pc = ip_to_pc[ip]
        response = ping(ip, count=1)
        if response.success():
            print(f"Successfully connected to {pc} ({ip})\n")
            # break
        else:
            print(f"Connection to {pc} ({ip})failed\n")
    else:
        print(f"Unknown IP Address: {ip}\n")

print("Finished checking IP addresses.\n")

input("Press enter to exit;")


# import subprocess

# # List of IP addresses to ping
# ip_addresses = ["192.168.1.2", "192.168.1.3", "192.168.1.4"]

# def check_connection(ip_address):
#     try:
#         output = subprocess.check_output(["ping", "-n", "1", ip_address], text=True)
#         if "Reply from" in output:
#             return True
#         return False
#     except subprocess.CalledProcessError:
#         return False

# for ip in ip_addresses:
#     if check_connection(ip):
#         print(f"Successfully connected to {ip}")
#         break
#     else:
#         print(f"Connection to {ip} failed")

# print("Finished checking IP addresses.")



# from pythonping import ping

# # List of IP addresses to ping
# ip_addresses = ["192.168.1.2", "192.168.1.3", "192.168.1.5"]

# desired_ttl = "TTL=255"

# for ip in ip_addresses:
#     response = ping(ip, count=1)
#     if response.success() and desired_ttl in str(response.output):
#         print(f"Successfully connected to {ip}")
#         break
#     else:
#         print(f"Connection to {ip} failed")

# print("Finished checking IP addresses.")




# import subprocess

# # List of IP addresses to ping
# ip_addresses = ["192.168.1.2", "192.168.1.3", "192.168.1.5"]

# desired_ttl = "TTL=255"

# for ip in ip_addresses:
#     try:
#         output = subprocess.check_output(["ping", "-n", "1", ip], text=True)
#         if desired_ttl in output:
#             print(f"Successfully connected to {ip}")
#             break
#         else:
#             print(f"Connection to {ip} failed")
#     except subprocess.CalledProcessError:
#         print(f"Error pinging {ip}")

# print("Finished checking IP addresses.")


# from pythonping import ping


# for ip, pc in ip_to_pc.items():
#     response = ping(ip, count=1)
#     if response.success():
#         print(f"Successfully connected to {pc} ({ip})")
#     else:
#         print(f"Connection to {pc} ({ip}) failed")

# print("Finished checking IP addresses.")



# import tkinter as tk
# from pythonping import ping

# # Dictionary mapping IP addresses to PC names
# ip_to_pc = {
#     "192.168.1.1": "NetGear",
#     "192.168.1.3": "Martin's PC",
#     "192.168.1.4": "My PC",
#     "192.168.1.5": "HCC BANANA"
# }

# def check_connections():
#     result_text.delete(1.0, tk.END)  # Clearinng previous results
#     for ip in ip_addresses: # iterates through each IP address in the ip_addresses list.
#         if ip in ip_to_pc:
#             pc = ip_to_pc[ip]
#             response = ping(ip, count=1)
#             if response.success():
#                 result_text.insert(tk.END, f"Successfully connected to {pc} ({ip})\n")
#             else:
#                 result_text.insert(tk.END, f"Connection to {pc} ({ip}) failed\n")
#         else:
#             result_text.insert(tk.END, f"Unknown IP Address: {ip}\n")
#     result_text.insert(tk.END, "Finished checking IP addresses.")

# # List of IP addresses to ping
# ip_addresses = [f"192.168.1.{i}" for i in range(1, 26)]

# root = tk.Tk()
# root.title("IP Checker")

# frame = tk.Frame(root)
# frame.pack(padx=20, pady=20)

# result_text = tk.Text(frame, height=10, width=40)
# result_text.pack(side=tk.LEFT)

# scrollbar = tk.Scrollbar(frame, command=result_text.yview)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# result_text.config(yscrollcommand=scrollbar.set)

# check_button = tk.Button(root, text="Check Connections", command=check_connections)
# check_button.pack(pady=10)

# root.mainloop()