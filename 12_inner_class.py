class Laptop:
    def __init__(self, brand, cpu_cores):
        self.brand = brand
        self.processor = self.Processor(cpu_cores)

    class Processor:
        def __init__(self, cores):
            self.cores = cores

        def display(self):
            print(f"Processor with {self.cores} cores.")

l = Laptop("Dell", 8)
l.processor.display()