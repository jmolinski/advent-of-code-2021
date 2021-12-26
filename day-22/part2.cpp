#include <unordered_map>
#include <set>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>

struct instruction {
    int x1, x2, y1, y2, z1, z2;
    bool on;
};

auto expand(std::set<int> const& pts) {
    std::vector<int> pts_vec(pts.begin(), pts.end());
    std::unordered_map<int, int> compressed;
    std::vector<int> dst;
    for (size_t i = 0; i < pts_vec.size(); ++i) {
        compressed.insert({pts_vec[i], i});
        if (i + 1 < pts_vec.size()) {
            dst.push_back(pts_vec[i + 1] - pts_vec[i]);
        }
    }

    return std::make_pair(compressed, dst);
}

int main() {
  std::set<int> xx, yy, zz;
  std::vector<instruction> instructions;

  std::ifstream input("/Users/jakubmolinski/dv/advent-of-code-2021/day-22/processed_input.txt");
  std::string line, on;
  while (std::getline(input, line)) {
    instruction i;
    std::stringstream ss(line);
    ss >> on >> i.x1 >> i.x2 >> i.y1 >> i.y2 >> i.z1 >> i.z2;
      i.on = on == "on";
    instructions.push_back(i);
  }

  for (const auto&i : instructions) {
      xx.insert(i.x1);
      xx.insert(i.x2 + 1);
      yy.insert(i.y1);
      yy.insert(i.y2 + 1);
      zz.insert(i.z1);
      zz.insert(i.z2 + 1);
  }

    auto [mx, dst_x] = expand(xx);
    auto [my, dst_y] = expand(yy);
    auto [mz, dst_z] = expand(zz);

    using triple = std::tuple<uint32_t, uint32_t, uint32_t>;
    std::set<triple> pts;
    for (const auto& i : instructions) {
        for (int x = mx[i.x1]; x < mx[i.x2 + 1]; ++x) {
            for (int y = my[i.y1]; y < my[i.y2 + 1]; ++y) {
                for (int z = mz[i.z1]; z < mz[i.z2 + 1]; ++z) {
                    if (i.on) {
                        pts.insert({x, y, z});
                    } else {
                        auto it = pts.find({x, y, z});
                        if (it != pts.end()) {
                            pts.erase(it);
                        }
                    }
                }
            }
        }
    }

    uint64_t result = 0;
    for (auto [x, y, z] : pts) {
        result += dst_x[x] * dst_y[y] * dst_z[z];
    }
    std::cout << result << std::endl;

    return 0;
}
