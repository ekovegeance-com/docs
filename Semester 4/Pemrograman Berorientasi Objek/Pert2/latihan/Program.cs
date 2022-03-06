namespace latihanOOP
{
	class Hero
	{
		string name;
		int health;
		double demage;
		bool isDead = false;

		public Hero(string name, int health, double demage)
		{
			this.name = name;
			this.health = health;
			this.demage = demage;
		}

		public void showHero()
		{
			Console.WriteLine($"==========={name}===========");
			Console.WriteLine("Name : {0}", name);
			Console.WriteLine("Health : {0}", health);
			Console.WriteLine("Demage : {0}", demage);
		}
	}


	class ItemHero
	{
		string nameItem;
		int healthItem;
		double demageItem;
		bool isEquip = false;

		public ItemHero(string nameItem, int healthItem, double demageItem)
		{
			this.nameItem = nameItem;
			this.healthItem = healthItem;
			this.demageItem = demageItem;
		}

		public void showItemHero()
		{
			Console.WriteLine($"==========={nameItem}===========");
			Console.WriteLine("Item Name : {0}", nameItem);
			Console.WriteLine("Item Health : {0}", healthItem);
			Console.WriteLine("Item Demage : {0}", demageItem);
		}
	}






	class Program
	{
		static void Main(string[] args)
		{
			Hero Alucard = new Hero("Alucard", 100, 10);
			ItemHero EndlessBattle = new ItemHero("Endless Battle", 10, 10);

			Hero Hayabusa = new Hero("Hayabusa", 100, 10);
			ItemHero BloodAxe = new ItemHero("Blood Axe", 10, 10);

			Alucard.showHero();
			Hayabusa.showHero();

			EndlessBattle.showItemHero();
			BloodAxe.showItemHero();

		}
	}
}
