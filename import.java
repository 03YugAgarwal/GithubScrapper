import java.util.Scanner;
class Pattern
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        for(int x=1;x<=n;x++)
        {
            for(int y=1;y<=x;y++)
            {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}