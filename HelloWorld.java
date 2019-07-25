/** java程序的简单应用：1.编译 javac HelloWorld.java--生成一个class程序 2. java HelloWorld 1 3 4 --1,3,4是输入的参数，会显示在shell中。 **/



public class HelloWorld {
    public static void main(String[] args) { /**args代表的是输入的参数，下面直接引用了。         **/
        System.out.println ( "Hollo World");
        for (int i=0;i<args.length;i++){
            System.out.println(args[i]);
        }
    }
}
