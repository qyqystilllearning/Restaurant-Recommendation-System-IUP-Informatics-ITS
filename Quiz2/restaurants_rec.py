import heapq
import math
import time
import itertools
from collections import deque

# Restaurant Dataset
restaurants = [
    {"name": "Kogu Space", "location": (-7.289284887207215, 112.77654179368488), "rating": 4.5, "price_range": "Rp25.000-50.000", "recommended": True},
    {"name": "Lao Ban", "location": (-7.26498963350016, 112.79558879656213), "rating": 4.4, "price_range": "Rp25.000-50.000", "recommended": True},
    {"name": "Ah Pek Kopitiam", "location": (-7.297132815252841, 112.78225586855604), "rating": 4.9, "price_range": "Rp25.000-50.000", "recommended": True},
    {"name": "Suprek Kertajaya", "location": (-7.279724415089022, 112.78064549553847), "rating": 4.8, "price_range": "Rp25.000-50.000"},
    {"name": "Ciamso", "location": (-7.275194686001927, 112.77321599553834), "rating": 4.7, "price_range": "Rp25.000-50.000"},
    {"name": "Mie Bangka Mulyosari", "location": (-7.267332782469328, 112.79764575506454), "rating": 4.3, "price_range": "Rp25.000-50.000", "recommended": True},
    {"name": "Expat. Roasters Surabaya", "location": (-7.270745471162421, 112.78228198164616), "rating": 4.4, "price_range": "Rp50.000–75.000", "recommended": True},
    {"name": "Choky Spaghetti & Coffee", "location": (-7.293444272410562, 112.80172925096215), "rating": 4.9, "price_range": "Rp25.000–50.000", "recommended": False},
    {"name": "Warung KANE", "location": (-7.288467823378114, 112.80147530863307), "rating": 4.8, "price_range": "Rp5.000–25.000"},
    {"name": "Nasi Padang Uda Wandi", "location": (-7.273952085413029, 112.75887006815299), "rating": 4.4, "price_range": "Rp10.000–50.000"},
    {"name": "Joder", "location": (-7.281154677076876, 112.78702342397513), "rating": 4.5, "price_range": "Rp10.000–25.000"},
    {"name": "FUKKURA Restaurant", "location": (-7.26410091011021, 112.77615855096172), "rating": 4.8, "price_range": "Rp25.000–50.000"},
    {"name": "Soto Ayam Lamongan CAK HAR", "location": (-7.289495066055176, 112.78323948164636), "rating": 4.5, "price_range": "Rp25.000–50.000"},
    {"name": "Bakso Mas Roy", "location": (-7.291933430864209, 112.78097216445553), "rating": 3.5, "price_range": "Rp25.000–50.000"},
    {"name": "Depot Terasa Nikmat Gubeng", "location": (-7.276197831847875, 112.75575283761599), "rating": 4.5, "price_range": "Rp25.000–50.000", "recommended": True},
    {"name": "Rumah Makan Idaman", "location": (-7.278816233398039, 112.76585672412466), "rating": 4.6, "price_range": "Rp25.000–50.000", "recommended": True},
    {"name": "Depot Pak Bas", "location": (-7.2813384195119335, 112.77210998179706), "rating": 4.3, "price_range": "Rp25.000–50.000", "recommended": True},
    {"name": "Sushi Hiro - Manyar Kertoarjo", "location": (-7.279873523315872, 112.77024708179695), "rating": 4.9, "price_range": "Rp100.000-200.000"},
    {"name": "Warung Leko Manyar", "location": (-7.277316729353046, 112.76603028179699), "rating": 4.6, "price_range": "Rp50.000–75.000"},
    {"name": "Foye Bistro", "location": (-7.266845754276976, 112.7689919952883), "rating": 4.9, "price_range": "Rp100.000-200.000"},
    {"name": "J-One", "location": (-7.287241464879591, 112.79456272397537), "rating": 4.5, "price_range": "Rp1.000-25.000"},
    {"name": "Warung Kampus", "location": (-7.288025858731019, 112.79270870052645), "rating": 4.5, "price_range": "Rp1.000-25.000"},
    {"name": "AADK", "location": (-7.289673535609158, 112.78830796650472), "rating": 4.7, "price_range": "Rp25.000-50.000"},
    {"name": "Rumah Makan Goyang Lidah", "location": (-7.290088033888297, 112.79714408419441), "rating": 4.6, "price_range": "Rp50.000-25.000"},
    {"name": "Ronggolawe Chicken Wonton Noodles", "location": (-7.267942736502967, 112.80457659881498), "rating": 4.6, "price_range": "Rp5.000-25.000"},
    {"name": "Sate Babi Mamaku", "location": (-7.265023821375838, 112.8059314527277), "rating": 4.3, "price_range": "Rp 40.000-90.000"},
    {"name": "Nasi Goreng Bin Ali", "location": (-7.268400, 112.796210), "rating": 4.8, "price_range": "Rp20.000-50.000", "recommended": True},
    {"name": "Kopi Titik Koma Grand Eastern", "location": (-7.291856, 112.811927), "rating": 4.8, "price_range": "Rp20.000-50.000", "recommended": True},
    {"name": "Thirty Three Brew", "location": (-7.274290053074575, 112.77550891001319), "rating": 4.8, "price_range": "Rp30.000-50.000", "recommended": True},
    {"name": "Tomoro Coffee", "location": (-7.268308972971302, 112.79618822503761), "rating": 4.8, "price_range": "Rp20.000-50.000"},
    {"name": "Drama Coffee & Roastery", "location": (-7.280944130412395, 112.77010932511416), "rating": 4.5, "price_range": "Rp50.000-75.000", "recommended": True  },
    {"name": "Bubur Kepagian", "location": (-7.289389382783312, 112.80024243144904), "rating": 4.8, "price_range": "Rp15.000-30.000"},
    {"name": "Bebek Sinjay Dharmahusada", "location": (-7.26779056950532, 112.771221310633), "rating": 4.3, "price_range": "Rp25.000-50.000"},
    {"name": "Manna Haus", "location": (-7.279829203382455, 112.78142122412457), "rating": 4.9, "price_range": "Rp100.000-200.000"},
    {"name": "Guri Ramen", "location": (-7.262922580479469, 112.79543278179682), "rating": 4.6, "price_range": "Rp25.000-50.000"},
    {"name": "Borre Cafe", "location": (-7.269121170260604, 112.77370945110744), "rating": 4.6, "price_range": "Rp50.000-100.000"},
    {"name": "Kedai Ori Manyar", "location": (-7.289308952557569, 112.77036436441765), "rating": 4.5, "price_range": "Rp25.000-50.000"},
    {"name": "Dimsum Mbeledos Merr", "location": (-7.259332336035753, 112.78262622227103), "rating": 4.4, "price_range": "Rp25.000-75.000"},
    {"name": "Restoran Padang Sederhana Kertajaya", "location": (-7.259332336035753, 112.78262622227103), "rating": 4.6, "price_range": "Rp25.000-75.000"},
    {"name": "HC Resto", "location": (-7.279830443446084, 112.77140183761617), "rating": 4.3, "price_range": "Rp25.000-50.000"},
    {"name": "Ruf Coffee & Eatery", "location": (-7.289321648385846, 112.77585030805459), "rating": 4.9, "price_range": "Rp25.000-50.000", "recommended": True},
    {"name": "Warung Ikan Cak Yu", "location": (-7.266252421985621, 112.7698520645988), "rating": 4.5, "price_range": "Rp25.000-50.000"},
    {"name": "Pawon Rempah Resto", "location": (-7.258895407203071, 112.78212230877953), "rating": 4.3, "price_range": "Rp50.000-75.000"},
    {"name": "Gokar Kencana Suterejo", "location": (-7.259097307279302, 112.78160783761585), "rating": 4.2, "price_range": "Rp25.000-50.000"},
    {"name": "Ayam Goreng Asli Pemuda Manyar", "location": (-7.279880864652926, 112.76556509343516), "rating": 4.4, "price_range": "Rp25.000-75.000", "recommended": True},
    {"name": "Bon Ami Restaurant Dharmahusada", "location": (-7.276533492738999, 112.77229513761614), "rating": 4.6, "price_range": "Rp50.000-100.000"},
    {"name": "Haewoo One Stop Korean Food", "location": (-7.27234159966066, 112.77356916459887), "rating": 4.8, "price_range": "Rp50.000-75.000", "recommended": True},
    {"name": "Second Cup Coffee", "location": (-7.272392414640401, 112.78217132412449), "rating": 4.7, "price_range": "Rp25.000-50.000"},
    {"name": "Depot Bu Rudy Dharmahusada", "location": (-7.267177982389897, 112.7701808259778), "rating": 4.5, "price_range": "Rp25.000-50.000"},
    {"name": "Ayam Goreng Ny. Suharti Gubeng", "location": (-7.276101086399509, 112.74571771063307), "rating": 4.5, "price_range": "Rp25.000-50.000"},
    {"name": "Cold 'N Brew Gubeng", "location": (-7.274398, 112.748321), "rating": 4.6, "price_range": "Rp25.000-50.000", "recommended": True},
     {"name": "Bebek Palupi Rungkut", "location": (-7.321966947550001, 112.77425382961697), "rating": 4.6, "price_range": "Rp 25.000-50.000", "recommended": True},
    {"name": "Waroeng Joglo Merah Putih", "location": (-7.342019389882795, 112.7855831591145), "rating": 4.5, "price_range": "Rp 25.000-50.000"},
    {"name": "Hotway's Chicken Surabaya Tenggilis", "location": (-7.318634917261419, 112.76300964129706), "rating": 4.6, "price_range": "Rp 25.000-50.000"},
    {"name": "Wizzmie Jemursari", "location": (-7.3105471999980915, 112.75732966613614), "rating": 4.8, "price_range": "Rp 25.000-50.000"},
    {"name": "Bakso dan Bakmie Asia Bangsa", "location": (-7.303548095754033, 112.75689408528564), "rating": 4.5, "price_range": "Rp 1-25.000"},
    {"name": "Kopitagram Tenggilis", "location": (-7.319951787194344, 112.75530311718603), "rating": 4.6, "price_range": "Rp 50.000-75.000"},
    {"name": "Toko Bakmie Saudagar", "location": (-7.320365171721056, 112.75985660933696), "rating": 4.3, "price_range": "Rp 25.000-50.000", "recommended": True},
    {"name": "Pangsit Mie Pinangsia", "location": (-7.319106507305015, 112.76523122304431), "rating": 4.5, "price_range": "Rp 25.000-50.000"},
    {"name": "Poenya Nyonya Anina Tenggilis", "location": (-7.320641719933456, 112.76158677157403), "rating": 4.6, "price_range": "Rp 25.000-50.000"},
    {"name": "Jatinangor House Gubeng", "location": (-7.289374297535545, 112.76238973749274), "rating": 3.8, "price_range": "Rp 25.000-50.000"},
    {"name": "Warung Salire", "location": (-7.289936121898199, 112.75229595604536), "rating": 4.6, "price_range": "Rp 1-25.000"},
    {"name": "Kopi Kakak Surabaya", "location": (-7.284738091573258, 112.75565728479945), "rating": 4.5, "price_range": "Rp 25.000-50.000"},
    {"name": "Kirei Lofekofe", "location": (-7.281734696331831, 112.7560005380588), "rating": 4.8, "price_range": "Rp 25.000-50.000"},
    {"name": "Pak Djo Meatball", "location": (-7.287656817669667, 112.76831038716074), "rating": 4.5, "price_range": "Rp 25.000-50.000"},
    {"name": "Nasi Goreng Kecap Pak Di", "location": (-7.289294543411621, 112.7727619963991), "rating": 4.5, "price_range": "Rp 1.000-25.000"},
    {"name": "Tahu Tek Ndublek", "location": (-7.331455170264893, 112.78484280865746), "rating": 4.4, "price_range": "Rp1.000-25.000"},
    {"name": "Warung Mbak Nar", "location": (-7.329284375950121, 112.79071148198636), "rating": 4.7, "price_range": "Rp 1.000-25.000"},
    {"name": "Pepper Skull Rungkut", "location": (-7.333359927139757, 112.7946167782932), "rating": 4.3, "price_range": "Rp 25.000-50.000"},
    {"name": "Kedai Sumber Nikmat", "location": (-7.33205107277073, 112.805367072033), "rating": 4.7, "price_range": "Rp 1.000-25.000"},
    {"name": "Bebek Omah Dewe", "location": (-7.336509674859979, 112.80461605351933), "rating": 4.6, "price_range": "Rp 1.000-25.000"},
    {"name": "Daidokoro Sushi Ramen Authentic", "location": (-7.337690824575698, 112.8021484212572), "rating": 4.8, "price_range": "Rp 25.000-75.000"},
    {"name": "Bento Kopi", "location": (-7.340987908616573, 112.78548694169443), "rating": 4.5, "price_range": "Rp 1.000-25.000"},
    {"name": "Warkop Revo 99", "location": (-7.343009674028711, 112.8025028756187), "rating": 4.4, "price_range": "Rp 1.000-25.000"},
    {"name": "808 Coffeebar", "location": (-7.330943664876716, 112.78864631627367), "rating": 4.7, "price_range": "Rp 1.000-25.000"},
    {"name": "Himec Coffee and Eatery", "location": (-7.323611862558192, 112.7857602594169), "rating": 4.5, "price_range": "Rp 25.000-50.000"},
    {"name": "Mr. Sumo Merr", "location": (-7.321302692224405, 112.78124341942011), "rating": 4.9, "price_range": "Rp 125.000-150.000"},
    {"name": "Toko Kopi Tuku Merr", "location": (-7.31599261935891, 112.78046021442672), "rating": 4.8, "price_range": "Rp 25.000-50.000"},
    {"name": "Wei Hong", "location": (-7.315258355824357, 112.79003033611383), "rating": 4.6, "price_range": "Rp 25.000-50.000"},
    {"name": "Delisiozo Surabaya", "location": (-7.316237373617299, 112.79455790495881), "rating": 4.8, "price_range": "Rp 50.000-75.000"},
    {"name": "Konka Coffee", "location": (-7.326794223279337, 112.7918961777398), "rating": 4.2, "price_range": "Rp 25.000-50.000"},
    {"name": "Kakkoii All You Can Eat Japanese", "location": (-7.280572726526857, 112.77099454073603), "rating": 4.7, "price_range": "Rp 125.000-175.000"},
    {"name": "WARUNG SOVIE", "location": (-7.295041197068976, 112.78133049375116), "rating": 3.9, "price_range": "Rp25.000-50.000"},
    {"name": "Warung Nanda", "location": (-7.297382428877375, 112.77935638794003), "rating": 4.6, "price_range": "Rp1.000-25.000"},
    {"name": "Seafood AMEN", "location": (-7.303625049319702, 112.78137125632294), "rating": 4.4, "price_range": "Rp75.000-100.000"},
    {"name": "D'Coffee Cup - Gunung Anyar", "location": (-7.340695931218665, 112.78577988642328), "rating": 2.9, "price_range": "Rp25.000-50.000"},
    {"name": "BM Coffee Surabaya - Merr", "location": (-7.325930011357331, 112.78087910733963), "rating": 4.1, "price_range": "Rp25.000-50.000"},
    {"name": "HONGER", "location": (-7.340582599883527, 112.7861010668352), "rating": 4.5, "price_range": "Rp25.000-50.000"},
    {"name": "Warkop DE PALLET", "location": (-7.341864888216235, 112.78632239023224), "rating": 4.5, "price_range": "Rp1.000-25.000"},
    {"name": "MOOGS Coffee", "location": (-7.322705148688577, 112.78046055091326), "rating": 4.6, "price_range": "Rp25.000-50.000"},
    {"name": "Ramen Master - Ir. Soekarno", "location": (-7.3231840083494495, 112.78068585645809), "rating": 4.5, "price_range": "Rp25.000-50.000"},
    {"name": "Warung 17", "location": (-7.317219065691251, 112.76295670488774), "rating": 4.5, "price_range": "Rp1.000-25.000"},
    {"name": "CARNIS", "location": (-7.3094435073938016, 112.76730724535147), "rating": 4.6, "price_range": "Rp30.000-100.000"},
    {"name": "Kampoeng Steak", "location": (-7.3050104476370095, 112.76922767265833), "rating": 4.4, "price_range": "Rp25.000-50.000"},
    {"name": "Bebek Carok - Surabaya", "location": (-7.294677822913461, 112.76267869085959), "rating": 4.6, "price_range": "Rp25.000-50.000"},
    {"name": "Toko Roti Cengli Manyar Rejo", "location": (-7.294662723202618, 112.7676206036722), "rating": 4.3, "price_range": "Rp25.000-50.000"},
    {"name": "Tip-Top Nasi Timbel", "location": (-7.278123554311434, 112.76560802694178), "rating": 4.4, "price_range": "Rp25.000-50.000"},
    {"name": "Ikan Bakar Cianjur - Manyar Kertoarjo", "location": (-7.278289841661771, 112.76557181712053), "rating": 4.6, "price_range": "Rp50.000-100.000"},
    {"name": "Flash Coffee", "location": (-7.277860405103996, 112.7656289554947), "rating": 4.6, "price_range": "Rp25.000-50.000"},
    {"name": "Yummy Resto", "location": (-7.277752221149269, 112.76535179700956), "rating": 4.7, "price_range": "Rp25.000-50.000"},
    {"name": "Thirty Bumbu by Chop Buntut Surabaya", "location": (-7.277821602206137, 112.76537657941401), "rating": 4.6, "price_range": "Rp50.000-75.000"},
    {"name": "Coste Coffee", "location": (-7.286038698157476, 112.75622387293582), "rating": 4.8, "price_range": "Rp25.000-Rp50.000", "recommended": True},
    {"name": "TBRK Roastery ", "location": (-7.288651262243083, 112.75269328644912), "rating": 4.6, "price_range": "Rp25.000–50.000", "recommended": True},
    {"name": "Kosaku Coffee Lab", "location": (-7.278223058383561, 112.76492986506334), "rating": 4.9, "price_range": "Rp30.000–75.000", "recommended": True},
    {"name": "Imba Coffee", "location": (-7.270652333783008, 112.79695952692026), "rating": 4.9, "price_range": "Rp25.000–50.000", "recommended": True},
    {"name": "Doux Butter", "location": (-7.265653488971702, 112.79609272691224), "rating": 4.8, "price_range": "Rp25.000-50.000"},
    {"name": "GNZA 100 - Coffee $ Bakery", "location": (-7.2890875898719, 112.75373398349483), "rating": 4.9, "price_range": "Rp50.000-75.000", "recommended": True},
    {"name": "KutuBuku Cafe", "location": (-7.291776458677413, 112.80173432876461), "rating": 4.9, "price_range": "Rp10.000-30.000"}
    ]

def calculate_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2) * 111

def check_budget(price_range, budget):
    price_range = price_range.replace("Rp", "").replace(".", "").replace("–", "-").split("-")
    max_price = int(price_range[1])
    return max_price <= budget

def heuristic(restaurant, preferred_rating):
    rating_score = 0 if restaurant['rating'] >= preferred_rating else (preferred_rating - restaurant['rating'])
    return rating_score

counter = itertools.count()

def a_star_search(user_location, restaurants, preferred_rating, max_distance, budget):
    # Step 1: Filter restaurants by preferred rating and budget, and sort by rating descending
    filtered_restaurants = sorted(
        [r for r in restaurants if r["rating"] >= preferred_rating and check_budget(r["price_range"], budget)],
        key=lambda r: r["rating"],
        reverse=True
    )

    queue = []
    # PUSH 5 ELEMEN! => (f_cost, counter, location, path, g_cost)
    heapq.heappush(queue, (0, next(counter), user_location, [], 0))
    visited = set()
    best_restaurants = []
    search_times = []

    while queue and len(best_restaurants) < 10:
        start_time = time.time()
        # POP 5 ELEMEN!
        f_cost, _, current_location, path, g_cost = heapq.heappop(queue)

        # Jika sudah mencapai node destinasi, tambahkan ke hasil
        if path:
            restaurant = path[-1]
            best_restaurants.append(restaurant)
            end_time = time.time()
            search_times.append((restaurant['name'], end_time - start_time))
            continue

        visited.add(current_location)

        for restaurant in filtered_restaurants:
            if restaurant["location"] in visited:
                continue

            distance = calculate_distance(current_location, restaurant["location"])
            if distance > max_distance:
                continue

            h_cost = heuristic(restaurant, preferred_rating)
            total_f_cost = g_cost + distance + h_cost

            new_path = path + [restaurant]
            heapq.heappush(queue, (total_f_cost, next(counter), restaurant["location"], new_path, g_cost + distance))

    return best_restaurants, search_times

def bfs(user_location, restaurants):
    queue = deque([(user_location, [])])
    visited = set()
    best_restaurants = []
    search_times = []

    for restaurant in sorted(restaurants, key=lambda r: calculate_distance(user_location, r["location"])):
        start_time = time.time()
        if restaurant["location"] in visited:
            continue

        distance = calculate_distance(user_location, restaurant["location"])
        visited.add(restaurant["location"])
        best_restaurants.append(restaurant)
        end_time = time.time()
        search_times.append((restaurant['name'], end_time - start_time))

        if len(best_restaurants) >= 5:
            break

    return best_restaurants, search_times
