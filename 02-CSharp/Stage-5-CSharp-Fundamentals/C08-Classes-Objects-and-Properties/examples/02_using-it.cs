var rex = new Dog("Rex", "Labrador");
var bella = new Dog("Bella", "Poodle");

rex.Bark();
bella.Play(30);
rex.Breed = "Lab";          // OK – has a setter
// rex.Name = "Max";        // compile error: read-only
// rex.energy = 99;         // compile error: private
