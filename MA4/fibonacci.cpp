#include <iostream>

class Person {
public:
    Person(int age) : age(age) {}

    int Person_fibonacci() {
        if (age <= 0) return 0;
        if (age == 1) return 1;
        int a = 0, b = 1;
        for (int i = 2; i <= age; i++) {
            int tmp = a;
            a = b;
            b = tmp + b;
        }
        return b;
    }

private:
    int age;
};

extern "C" {
    Person* create_person(int age) {
        return new Person(age);
    }

    void delete_person(Person* person) {
        delete person;
    }

    int Person_fibonacci(Person* person) {
        return person->fibonacci();
    }
}
