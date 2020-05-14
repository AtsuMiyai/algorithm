//説明はABC157 youtube
#include <bits/stdc++.h>
using namespace std;
#define ll long long

struct UnionFind
{
    vector<int> d; //データを持つ。リンクの情報とサイズの情報
    //リンクがあるなら親のID
    //根なら-のサイズ
    //非負なら子である。
    UnionFind(int n) : d(n, -1) {} //コンストラクタはそのクラスのオブジェクトを初期化するために使われる。
    //初期化の意味　最初は全て-1＝全員根でサイズ1。
    int find(int x)
    {
        if (d[x] < 0) //もし今の頂点が根ならその頂点番号を渡す。
        {
            return x;
        }
        return find(d[x]); //根でないなら、親を探すように指示を送る。
        //経路縮約(メモ化)を行うと　return d[x]=find(d[x]);
    }
    bool unite(int x, int y) //二つ頂点を持ってきてこれらをくっつける。
    {
        x = find(x);
        y = find(y); //初期状態では両方を根とする。x,yは根(親)のid
        if (x == y)
        {
            return false; //クラスカル法の時に使うらしい
        }
        if (d[x] > d[y])
        {
            swap(x, y);
        }
        d[x] += d[y]; //xにyをくっつける。サイズの小さい方を大きい方にくっつけること！！
        d[y] = x;     //親のidに張り替える。
        return true;
    }
    bool same(int x, int y) //同じ集合に属しているかどうか.

    {
        return find(x) == find(y);
    }
    int size(int x)
    {
        return -d[find(x)];
    }
};
