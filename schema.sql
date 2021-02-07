drop table if exists schedules;
	create table schedules (
		id integer primary key autoincrement,
        dateNum text not null,
		fname text not null,
		lname text not null,
        email text not null
);
