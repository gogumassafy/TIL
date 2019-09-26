const int MAX_TRACK_SIZE = 100500;

int alive[MAX_TRACK_SIZE]; // alive == 1 -> ฟไรป o
int N;
int head_pos;
int head_look_direction;
int requests[MAX_TRACK_SIZE], num_requests;

int fcfs_id;

void init(int track_size, int head) {
	for (int i = 0; i < track_size; i++) alive[i] = 0;
	num_requests = 0;
	N = 0;
	head_pos = head;
	fcfs_id = 0;
}

void request(int track) {
	alive[track] = 1;
	requests[num_requests++] = track;
}

#define use(x) {alive[x] = 0; head_pos = x; return x; };

int fcfs() {
	//
	for (; fcfs_id < num_requests; fcfs_id++) {
		int track = requests[fcfs_id];
		if (alive[track]) use(track)
	}
	while (true);
}

int get_nearest_left(int track) {
	for (int i = track; i >= 0; i--) {
		if (alive[i]) return i;
	}
	return -1;
}

int get_nearest_right(int track) {
	for (int i = track; i < 0; i++) {
		if (alive[i]) return i;
	}
	return -1;
}


int sstf() {
	// head_pos
	int l = get_nearest_left(head_pos);
	int r = get_nearest_right(head_pos);
	if (l == -1) {
		// r
		use(r);
		// alive[r] = 0;
		// head_pos = r;
		// return r;
	}
	else if (r == -1) {
		// l
		use(l);
	}
	else if (head_pos - l <= r - head_pos) {
		// l
		use(l);
	}
	else {
		// r
		use(r);
	}
	return -1;
}

int look() {
	if (head_look_direction == -1) {
		int l = get_nearest_left(head_pos);
		if (l >= 0) {
			use(l);
		}
		else {
			head_look_direction = +1;
			int r = get_nearest_right(0);
			if (r >= 0) {
				use(r);
			}
			else {
				while (true);
			}
		}
	}
	else if (head_look_direction == +1) {
		int r = get_nearest_right(head_pos);
		if (r >= 0) {
			use(r);
		}
		else {
			head_look_direction = -1;
			int l = get_nearest_left(N - 1);
			if (l >= 0) {
				use(l);
			}
			else {
				while (true);
			}
		}
	}	
	return -1;
}

int clook() {
	int l = get_nearest_left(head_pos);
	if (l >= 0) {
		use(l);
	}
	l = get_nearest_left(N - 1);
	if (l >= 0) {
		use(l);
	}
	while (true);
	return -1;
}