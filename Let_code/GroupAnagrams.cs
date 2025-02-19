namespace Let_code
{
    public class GroupAnagrams
    {
        public static void Group(string[] strs)
        {
            Dictionary<string, List<string>> hashMapAnagrams = [];

            foreach (string word in strs)
            {
                string key = string.Join("", word.OrderBy(letter => letter));

                if(hashMapAnagrams.TryGetValue(key, out List<string>? value))
                {
                    value.Add(word);
                }
                else
                {
                    hashMapAnagrams.Add(key, [word]);
                }
            }

            foreach (var item in hashMapAnagrams)
            {
                foreach (var word in item.Value)
                {
                    Console.Write(word + " ");
                }
                Console.WriteLine();
            }
        }
    }
}