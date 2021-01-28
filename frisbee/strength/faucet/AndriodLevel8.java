package frisbee.strength.faucet;

public class AndriodLevel8 {
   private static byte[] a = new byte[] { 50, 55, 98, 101, 99, 51, 56, 53, 99, 52, 48, 57, 52, 98, 48, 54, 98, 51, 101,
         101, 51, 48, 54, 100, 57, 49, 102, 55, 50, 56, 53, 98 };
   private static final byte[] b = new byte[] { -47, 25, 37, 82, -94, -20, -61, -96, -10, -81, 17, 89, -56, -111, -113,
         67, 29, -59, -125, 92, -127, 40, -120, -33, 13, -88, -35, -46, 77, 64, 1, 109, -85, 125, -1, -94, 90, 116,
         62 };
   private final byte[] c = new byte[256];
   private final byte[] d = new byte[256];

   private AndriodLevel8(byte[] var1) {
      byte var2 = 0;

      int var3;
      for (var3 = 0; var3 < 256; ++var3) {
         this.c[var3] = (byte) ((byte) var3);
         this.d[var3] = (byte) var1[var3 % var1.length];
      }

      int var4 = 0;

      for (var3 = var2; var3 < 256; ++var3) {
         var1 = this.c;
         var4 = var4 + var1[var3] + this.d[var3] & 255;
         byte var5 = var1[var3];
         var1[var3] = (byte) var1[var4];
         var1[var4] = (byte) var5;
      }

   }

   private byte[] a(byte[] var1) {

      byte[] var2 = new byte[var1.length];

      for (int var3 = 0; var3 < 4; ++var3) {
         int var4 = 0;
         int var5 = 0;

         for (int var6 = 0; var4 < var1.length; ++var4) {
            var5 = var5 + 1 & 255;
            byte[] var7 = this.c;
            var6 = var6 + var7[var5] & 255;
            byte var8 = var7[var5];
            var7[var5] = (byte) var7[var6];
            var7[var6] = (byte) var8;
            var2[var4] = (byte) ((byte) (var7[var7[var5] + var7[var6] & 255] ^ var1[var4]));
         }
      }
      return var2;
   }

   public static String verify() {
      byte[] var1 = (new AndriodLevel8(a)).a(b);

      String s = new String(var1);

      return s;
   
   }
   public static void main(String[] args) {
      System.out.println(verify());
   }
}
