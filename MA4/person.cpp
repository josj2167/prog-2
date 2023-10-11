#include <cstdlib>
#include <iostream>
// Person class 

class Person {
public:
	Person(int);
	int get();
	void set(int);
	int fib();
private:
	int age;
	int fib_rec(int n);
	
};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}

int Person::fib() {
	return this -> fib_rec(this->age)
}

int Person::fib_rec(int n) {
    if (n <= 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            int temp = a;
            a = b;
            b = temp + b;
        }
        return b;
    }
}
extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	int Person_fib(Person* person)
	{
		return person -> fib();

	}
	}
