extern void MyPrintf(const char *mainFunName, const char *slaveFunName);
extern int MyTest();

int main()
{
    MyTest();

    MyPrintf("I am main", "I am salve");

    return 0;
}