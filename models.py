class Beds:
    def __init__(self, building: int, room: int, bed: int):
        self.building = building
        self.room = room
        self.bed = bed
        self.soldier_id = None

def create_list_of_nums(num_buildings: int, num_rooms: int, num_beds: int) -> list[int]:
    list_of_nums = []
    for i in range(1, num_buildings+1):
        for j in range(1, num_rooms+1):
            for k in range(1, num_beds+1):
                l = [i, j, k]
                list_of_nums.append(l)
    return list_of_nums

def create_bed_object():
    all_beds = create_list_of_nums(2,10,8)
    beds = []
    for b in all_beds:
        beds.append(Beds(b[0], b[1], b[2]))
    return beds




