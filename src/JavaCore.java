import java.util.Scanner;

public class JavaCore {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.nextLine();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = in.nextInt();
        }
        if (n == 1 && arr[0] == 1) {
            System.out.println(1);
            return;
        }
        long res = 0;
        long m = 1000000007;
        for (int i = 0; i < n; i++) {
            long temp = arr[i] * (arr[i] + 1) / 2;
            res = (res + temp) % m;
        }
        for (int j = 1; j < n - 1; j++) {
            int i = 1;
            while (j - i >= 0 && j + i < n) {
                long l = arr[j - i];
                long r = arr[j + i];
                res = (res + Math.min(l, r)) % m;
                i += 1;
                if (l != r)
                    break;
            }
        }
        System.out.println(res);
    }

    public class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;
        }
    }

    public boolean isBalanced(TreeNode node) {
        return (boolean) recur(node)[0];
    }

    public Object[] recur(TreeNode node) {
        if (node == null)
            return new Object[]{true, 0};
        Object[] left = recur(node.left);
        Object[] right = recur(node.right);
        if (!((boolean) left[0]) || !((boolean) right[0]) || Math.abs((int) left[1] - (int) right[1]) > 1)
            return new Object[]{false, 0};
        return new Object[]{true, Math.max((int) left[1], (int) right[1]) + 1};
    }

    public boolean isSubtree(TreeNode s, TreeNode t) {
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        preOder(s, sb1);
        preOder(t, sb2);
        if(sb1.toString().contains(sb2.toString()))
            return true;
        return false;
    }
    public void preOder(TreeNode node, StringBuilder sb){
        if(node == null){
            sb.append("#");
            return;
        }
        sb.append(node.val).append("-");
        preOder(node.left, sb);
        preOder(node.right, sb);
    }
}