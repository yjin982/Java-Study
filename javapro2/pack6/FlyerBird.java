package pack6;

public class FlyerBird implements Flyer{
	
	@Override
	public void fly() {
		System.out.println("날개를 휘저으며 숲 속으로 날아감");
	}
	public boolean isAnimal() {
		return true;
	}
	
}
