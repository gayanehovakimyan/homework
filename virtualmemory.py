def initialize_memory(num_frames):
    return [None] * num_frames, {}

def allocate_page(memory, page_number, page_size):
    frames, page_table = memory

    if page_number in page_table:
        print(f"Page {page_number} is already in memory.")
        return memory

    if len(page_table) < len(frames):
        available_frame = frames.index(None)
        frames[available_frame] = page_number
        page_table[page_number] = available_frame
        print(f"Allocated Page {page_number} to Frame {available_frame}")
    else:
        
        page_to_evict = frames[0]
        frames = frames[1:] + [page_number]
        evicted_frame = page_table.pop(page_to_evict)
        page_table[page_number] = evicted_frame
        print(f"Allocated Page {page_number} to Frame {evicted_frame}, evicting Page {page_to_evict}")

    return frames, page_table

def access_page(memory, page_number):
    frames, page_table = memory

    if page_number not in page_table:
        print(f"Page {page_number} is not in memory. Loading...")
        memory = allocate_page(memory, page_number, page_size=4)

    frame_number = page_table[page_number]
    print(f"Accessing Page {page_number} in Frame {frame_number}")

def display_memory_status(memory):
    frames, page_table = memory
    print("\nMemory Status:")
    for i in range(len(frames)):
        print(f"Frame {i}: ", end="")
        if frames[i] is not None:
            print(f"Page {frames[i]}", end="")
        else:
            print("Empty", end="")
        print()
    print()


