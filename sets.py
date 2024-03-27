#1
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
same_desination = our_routes.intersection(competitor_routes)
special_to_us = our_routes.difference(competitor_routes)
special_to_them = competitor_routes.difference(our_routes)
neither_share = our_routes.symmetric_difference(competitor_routes)

print(same_desination)
print(special_to_us)
print(special_to_them)
print(neither_share)

#2
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
new_id_list = list(set(customer_ids))
print(new_id_list)

