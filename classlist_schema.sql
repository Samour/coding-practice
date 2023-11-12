create table teacher(
    id          int primary key,
    "name"      varchar
);

create table student(
    id          int primary key,
    "name"      varchar
);

create table school_class(
    id          int primary key,
    code        varchar,
    "year"      varchar,
    "name"      varchar,
    teacher_id  int,

    constraint fk_teacher_id foreign key
        (teacher_id) references teacher(id)
);

create table school_class_student(
    class_id    int,
    student_id  int,

    constraint pk_school_class_student primary key
        (class_id, student_id),
    constraint fk_class_id foreign key
        (class_id) references school_class(id),
    constraint fk_student_id foreign key
        (student_id) references student(id)
);
