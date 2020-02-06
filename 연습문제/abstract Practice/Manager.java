package pack4;

public class Manager extends Regular{
	private double incentive = 0;
	
	public Manager() {}
	public Manager(String irum, int nai, int salary) {
		super(irum, nai, salary);
	}
	
	@Override
	public double pay() {
		if(super.pay() >= 2500000)
			incentive = super.pay()* 0.6;
		else if(super.pay() >= 200000)
			incentive = super.pay() * 0.5;
		else
			incentive = super.pay() * 0.4;
		
		return incentive+super.pay();
	}
	@Override
	public void print() {
		display();
		System.out.println("수령액 : " + this.pay());
	}
}

