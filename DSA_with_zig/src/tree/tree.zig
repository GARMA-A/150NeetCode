const std = @import("std");
pub fn BSTree(comptime T: type) type {
    return struct {
        const Self = @This();
        const Node = struct {
            data: T,
            left: ?*Node,
            right: ?*Node,
        };

        alloc: std.mem.Allocator,
        head: ?*Node,

        pub fn init(allocator: std.mem.Allocator) Self {
            return Self{ .head = null, .alloc = allocator };
        }
        pub fn push(self: *Self, value: T) !void {
            const newNode = self.alloc.create(Node) catch return;
            newNode.left = null;
            newNode.right = null;
            newNode.data = value;

            var cur = self.head orelse {
                self.head = newNode;
                return;
            };
            while (cur) {
                if (value < cur.data and cur.left) {
                    cur = cur.left;
                } else if (value < cur.data) {
                    cur.left = newNode;
                    break;
                }

                if (value >= cur.data and cur.right) {
                    cur = cur.right;
                } else if (value >= cur.data) {
                    cur.right = newNode;
                    break;
                }
            }
        }

        pub fn display(_: Self, curNode: *Node) void {
            std.debug.print("{d} ,", .{curNode.data});
            if (curNode.left != null)
                display(curNode.left);

            if (curNode.right != null)
                display(curNode.right);
        }
    };
}
